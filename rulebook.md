---
layout: page
title: Dynamic 7 Wonders rulebook
toc: true
toc_stop_autofire: true
---

<script type="text/javascript">

function toggleEd() {
  return toggle('#edition');
}

function toggle(id) {
  if (readCheckbox(id)) { 
    $(id).prop('checked', false);
  } else { 
    $(id).prop('checked', true);
  }
  flipSwitches();
  return false; 

}

function readCheckbox(id) {
  return $(id).is(':checked')
}

function enable(id) {
  $(id).removeAttr('disabled');
}

function forbidCheckbox(id) {
  $(id).prop('checked', false)
       .prop('disabled', true);
}

function mandateCheckbox(id) {
  $(id).prop('checked', true)
       .prop('disabled', true);
}


function forbidMenu(id) {
  $(id).prop('disabled', true);
  if ( $(id).is(':selected')) {
    $(id).removeAttr('selected');
  }
}

function validateForm() {
  if (readCheckbox('#pegasus')) {
    enable('#newcaprica');
    enable('#forceexodus');
  } else {
    forbidCheckbox('#forceexodus');
    forbidMenu('#newcaprica');
  }
  // Exodus checkboxes only allowed with Exodus.
  if ( readCheckbox('#exodus') ) {
    // Enable those boxes
    enable('#personalgoal');
    enable('#finalfive');
    enable('#cylonfleet');
    enable('#forcepegasus');
    enable('#ioniannebula');
  } else {
    // Disable them and also make sure they're not checked.
    forbidCheckbox('#personalgoal');
    forbidCheckbox('#finalfive');
    forbidCheckbox('#cylonfleet');
    forbidCheckbox('#forcepegasus');
    forbidMenu('#ioniannebula');
  }
  if ( $('#ioniannebula').is(':selected')
       || $('#allendings').is(':selected')
       || ! readCheckbox('#exodus') ) {
    forbidCheckbox('#allyseasons');
  } else {
    enable('#allyseasons');
  }
}

function highlight(theClass) {
  // Don't highlight the "no" classes, except for "nosympathizer"
  if (theClass === "nosympathizer" || ! /^no/.test(theClass)) {
    $('.' + theClass).css({"background-color":"lightyellow"});
  }
}

function unhighlight(theClass) {
  $('.' + theClass).css({"background-color":""});
}

function flipSwitches () {
  // Step 1: validate the form. Uncheck and disable items that aren't
  // allowed.
  
  validateForm();
  
  // Step 2: Collect lists of classes to hide and show.
  var showThese = [];
  var hideThese = [];
  var pullFrom = 'input,option';
  //if (readCheckbox('#allendings')) {
    // Actually, don't read the endings, we'll do that now.
    pullFrom = 'input';
  //}
  
  $(pullFrom).each(function(index, element) {
    if ($(this).is(':checked')) {
      showThese.push($(this).attr('id'));
      hideThese.push('no-'+$(this).attr('id'));
    } else {
      showThese.push('no-'+$(this).attr('id'));
      hideThese.push($(this).attr('id'));
    }
  });  
      
  // Step 3: Show all the classes that need showing. 
  for (i in showThese) {
    $('.'+showThese[i]).show();
    // Highlight if requested
    if (readCheckbox('#highlight')) {
      highlight(showThese[i]);
    } else {
      unhighlight(showThese[i]);
    }
  }
  // Step 4: Hide all the classes that need hiding. Since we do this 
  // last, that means a given tag needs *all* elements to be visible,
  // or in other words, each list of tags is ANDed together.
  for (i in hideThese) {
    $('.'+hideThese[i]).hide();
  }
  
  // Step 5: Fix the rowspan on the basestar attack table. It has to
  // change based on the options set.
  var rowspan = 3;
  if (readCheckbox('#daybreak')) {
    // Additional one for assault raptors
    rowspan++;
  }
  if ( readCheckbox('#cylonfleet')) {
    // Remove the nuke row
    rowspan--;
  }
  $('#basestardamage').attr('rowspan', rowspan);
    
  // Step 5: Refresh the table of contents.
  $('#toc').toc({showSpeed: 0});
  
  // Save to local storage
  save();
  
  // Update the share URL box
  var url = window.location.origin + window.location.pathname + "?" + buildStateString();
  $('#generatedUrl').val(url);

}

function save() {
  if (window.sessionStorage){
    try {
      $('input,option').each(function(index, element) {
        if (readCheckbox('#'+$(this).attr('id') )) { 
          window.sessionStorage.setItem($(this).attr('id'), "1");
        } else {
          window.sessionStorage.removeItem($(this).attr('id'));
        }
      });  
    } catch (err) {
      // Probably not allowed. That's okay, this
      // feature is optional so silently failing
      // is okay. 
    }
  }
}

// find all the selected / checked items and return a
// querystring representing them
function buildStateString() {
  qs = [];
  $('input,option').each(function(index, element) {
    id = $(this).attr('id');
    if (readCheckbox('#' + id)) {
      qs.push(id);
    }
  });
  return qs.join('&');
}

// enable this id (check it or select it)
function setValue(id) {
  if (!/^[a-zA-Z][a-zA-Z0-9\-\_]+$/.test(id)) {
    return false;
  }
  var el = $('#'+id);
  
  if (el.length === 0) {
    return false;
  }
  
  if (el.is('option') || el.is('input')) {
    el.prop('checked', true);
    el.prop('selected', true);

    return true;
  }
  
  return false;
}

// Make checkboxes mutually exclusive, so you can uncheck them, what you can't do with radio buttons
function toggleExclusive(clicked) {
  document.querySelectorAll('input[name="' + clicked.name + '"]').forEach(box => {
    if (box !== clicked) box.checked = false;
  });
}

// This is the page initialization code
$(function () {
  // Obviously, we have JavaScript if this is running.
  $(".nojs").hide();
  $(".js").show();

  var foundConfig = false;
  // queryparam exists?
  var qs = window.location.search;
  if (!!qs) {
    // use querystring to set values
    qs = qs.replace("?", '').split('&');
    for (var i=0; i < qs.length; i++) {
      if (setValue(qs[i])) {
        foundConfig = true;
      }
    }
  }
  
  if (foundConfig) {
    // Disable configuration, since this is preconfigured.
    // But they can choose to remove the configuration if desired.
    $(".preconfigured").show();
    $(".nopreconfigured").hide();
  } else {
    // state exists?
    if (window.sessionStorage){
      for (id in window.sessionStorage) {
        setValue(id);
      }
    }
    // Show the real config form
    $("#configform").show();
    // There is no preconfiguration here. Set CSS accordingly.
    $(".preconfigured").hide();
    $(".nopreconfigured").show();

  }
  $('#configform').change(flipSwitches);
  flipSwitches();
});

</script>

<form id="configform" style="display: none;">
  <fieldset id="configbox">
    <legend>Configuration:</legend>
    <label><input type="radio" name="edition" id="Ed1" checked> 1st Edition</label>
    <label><input type="radio" name="edition" id="Ed2"> 2nd Edition</label>
    <hr>
    <legend>Wonders</legend>
    <label><input type="checkbox" name="wonderpack" id="wonderpack"> Wonder Pack</label><br>
    <label><input type="checkbox" name="catan" id="catan"> Catan Wonder</label><br>
    <hr>
    <label><input type="checkbox" name="leaders" id="leaders"> Leaders</label><br>
    <div style="margin-left: 20px" class="leaders">
        <label><input type="checkbox" name="leaders-anniversary" id="leaders-anniversary">Leaders Anniversary Pack</label>        
        <label><input type="checkbox" name="esteban" id="esteban">Esteban</label>
        <label><input type="checkbox" name="linus" id="linus">Linus</label>
        <label><input type="checkbox" name="louis" id="louis">Louis</label>
        <label><input type="checkbox" name="nimrod" id="nimrod">Nimrod</label>
        <label><input type="checkbox" name="stevie" id="stevie">Stevie</label>
        <label><input type="checkbox" name="wil" id="wil">Wil</label> 
    </div>
    <label><input type="checkbox" name="cities" id="cities"> Cities</label><br>
    <div style="margin-left: 20px" class="cities">
        <label><input type="checkbox" name="cities-anniversary" id="cities-anniversary">Cities Anniversary Pack</label>
    </div>
    <label><input type="checkbox" name="babeledifice" id="babel"> Babel</label><br>
    <div style="margin-left: 20px" class="babel">
        <label><input type="checkbox" name="tower" id="tower"> Babel Tower</label>
        <label><input type="checkbox" name="greatprojects" id="greatprojects"> Babel Great Projects</label>
    </div>
    <label><input type="checkbox" name="babeledifice" id="edifice"> Edifice</label><br>
    <label><input type="checkbox" name="armada" id="armada"> Armada</label><br>
    <div style="margin-left: 20px" class="armada">
        <label><input type="checkbox" name="siracusa" id="siracusa">Siracusa Wonder</label>
    </div>
    <label>Share this configuration: 
      <input style="width: 100%;" type="text" id="generatedUrl" name="generatedUrl" />
    </label>
  </fieldset>
</form>

<form id="preconfigform" class="preconfigured" style="display: none;">
    <fieldset id="preconfigbox">
        <legend>Configuration:</legend>
        <p>This link was pre-configured. <a href="{{ site.baseurl }}rulebook.html">
        Click here to go back to the configurable rulebook</a></p>

        <p>
        This configuration includes:</p>
        <ul>
            <li class="Ed1">1st Edition</li>
            <li class="Ed2">2nd Edition</li>
        </ul>
        <ul>
            <li class="wonderpack">Wonder Pack</li>
            <li class="catan">Catan</li>
        </ul>
        <ul>
            <li class="leaders">Leaders<span class="leaders-anniversary"> and Leaders Anniversary Pack</span></li>
            <li class="cities">Cities<span class="cities-anniversary"> and Cities Anniversary Pack</span></li>
            <li class="babel">Babel
            <ul>
                <li class="tower">Babel Tower</li>
                <li class="greatprojects">BabelGreat Projects</li>
            </ul></li>
            <li class="edifice">Edifice</li>
            <li class="armada">Armada</li>
        </ul>
    </fieldset>
</form>

<form id="nojsform" class="nojs">
  <fieldset id="preconfigbox">
    <legend>Configuration:</legend>
    <p>JavaScript is either not enabled or not working. The rules for 
    including every expansion, with no variants enabled, will
    be shown instead, along with the rules for each possible ending. </p>
  </fieldset>
</form>

{% include toc.html %}

## Introduction

## The basics

## Game setup

## Turn order

### Start of Age

#### Turn Resolution

### End of Age
<ol>
	<li class="babel greatprojects">Check the completion status of the Great Project
		<ul>
			<li><strong>The Great Project is a success. </strong> If all participation tokens have been taken all players who participated gain as many reward tokens as they have participation tokens in their possession. The participation tokens are returned to the supply. </li>
			<li><strong>The Great Project is a failure. </strong>If there are remaining tokens on the Great Project card, those players without a participation token suffer the penalty displayed on the Great Project card. The participation are returned to the supply. </li>
		</ul>		
	</li>
	<li>Resolve <span class="no-armada">Military</span><span class="armada">Ground</span> Conflict. Award bonus and penalty points comparing your <span class="no-armada">military strength</span><span class="armada">Ground Shields</span> to your left and right neighbors'<span class="armada"> and players you've given an incursion token to (diplomacy tokens do not affect boarding tokens)</span>. In case of tie no one gets a bonus/penalty token. <span class="cities">If you have a diplomacy token, you do not participate in military conflicts and your neighbors to your left and right compare each other as if they were adjacent. Discard the diplomacy token after the resolution of all conflicts. </span>
  </li>
	<li class="armada">Resolve Naval conflicts. Award bonus and penalty tokens. The comparison is done among all players. The weakest Naval Strength gets a penalty bonus, then the strongest, second and third get the corresponding bonuses, in that order. 
  <div markdown="1">
  | Age | Weakest | Strongest | 2nd Strongest | 3rd Strongest |
  |:---:|:---:|:---:|:---:|:---:|
  | I | -1 | 3 | 1 | |
  | II | -2 | 5 | 3 | |
  | III | -3 | 7 | 5 | 3 |
  </div>
  <p>In case of a tie for the weakest, both players take a Naval Defeat token. In case of a tie for the strongest, both players take the reward of the next rank, and the second goes down to the third rank. In case of a tie in second strongest, both players go down to third rank and the player(s) in third position get no bonus tokens.</p>
	</li>
</ol>
<p>Each Guild Card is limited to a maximum of 10 points. </p>

If multiple players take cards from the discard pile during a single turn, the resolution order is:
<ol>
  <li>Halikarnassos</li>
  <li class="wonderpack">The Great Wall</li>
  <li class="wonderpack">Manneken Pis</li>
  <li class="leaders">Solomon</li>
  <li class="cities">Counterfeiter's Office</li>
  <li>Courtesans Guild</li>
</ol>
