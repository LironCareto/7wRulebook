---
layout: page
title: Dynamic 7 Wonders rulebook
toc: true
toc_stop_autofire: true
---

<script type="text/javascript">

function toggleEd() {
  return toggle('#cylonleader');
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
  
  // Loyalty deck styles only apply in certain scenarios
  if ($('#ioniannebula').is(':selected')
       || readCheckbox('#allyseasons') 
       || readCheckbox('#personalgoal')) {
     // Exodus style is required.
     forbidCheckbox('#forcepegasus');
     forbidCheckbox('#forceexodus');
   }
  
  if (readCheckbox('#forceexodus')) {
    // Obviously can't have both on at the same time
    forbidCheckbox('#forcepegasus');
  } else if (readCheckbox('#forcepegasus') || readCheckbox('#exodus')) {
    // Also, no point in "forcing" Exodus if it's already on
    forbidCheckbox('#forceexodus');
  }
  
  if (readCheckbox('#daybreak')) {
    enable('#searchforhome');
    if ( ! $('#searchforhome').is(':selected')
         && ! $('#allendings').is(':selected')) {
      enable('#forcedemetrius');
    } else {
      forbidCheckbox('#forcedemetrius');
    }
  } else {
    forbidMenu('#searchforhome');
    forbidCheckbox('#forcedemetrius');
  }
  if (readCheckbox('#pegasus') || readCheckbox('#daybreak')) {
    enable('#cylonleader');
  } else {
    forbidCheckbox('#cylonleader');
  }
  
  if (readCheckbox('#cylonleader') || readCheckbox('#daybreak')) {
    // Sympathizer rules don't apply
    forbidCheckbox('#nosympathizer');
    forbidCheckbox('#sympatheticcylon');
  } else {
    enable('#nosympathizer');
    enable('#sympatheticcylon');
  }
  if (readCheckbox('#sympatheticcylon')) {
    forbidCheckbox('#nosympathizer');
  } else if (readCheckbox('#nosympathizer')) {
    forbidCheckbox('#sympatheticcylon');
  }
  
  if (! readCheckbox('#daybreak') &&
        (readCheckbox('#cylonleader') || readCheckbox('#sympatheticcylon'))) {
    // Agenda cards are possible, might want to override
    enable('#forcemotive');
  } else {
    forbidCheckbox('#forcemotive');
  }
  
  if (readCheckbox('#daybreak') || readCheckbox('#pegasus')
      || readCheckbox('#sympatheticcylon')) {
    forbidCheckbox('#forceoverlay');  
  } else {
    enable('#forceoverlay');
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
    showThese = ['cities', 'leaders', 'babel', 'armada'];
    hideThese = ['no-cities', 'no-leaders', 'no-babel', 'no-armada'];
  //}
  
  $(pullFrom).each(function(index, element) {
    if ($(this).is(':checked')) {
      showThese.push($(this).attr('id'));
      hideThese.push('no'+$(this).attr('id'));
    } else {
      showThese.push('no'+$(this).attr('id'));
      hideThese.push($(this).attr('id'));
    }
  });  
  
  if (readCheckbox('#daybreak') 
      || readCheckbox('#pegasus')
      || readCheckbox('#exodus')) {
    showThese.push('expansion');
    hideThese.push('noexpansion');
  } else {
    showThese.push('noexpansion');
    hideThese.push('expansion');
  }
  
  if (readCheckbox('#pegasus') || readCheckbox('#exodus')) {
    showThese.push('execution');
    hideThese.push('noexecution');
  } else {
    showThese.push('noexecution');
    hideThese.push('execution');
  }

  // Exodus loyalty if either:
  //    Exodus is enabled, and hasn't been forced off
  //    Or we've forced Exodus rules to be on
  if ( (readCheckbox('#exodus') && ! readCheckbox('#forcepegasus'))
       || readCheckbox('#forceexodus')) {
    showThese.push('exodusloyalty');
    hideThese.push('noexodusloyalty');
  } else {
    showThese.push('noexodusloyalty');
    hideThese.push('exodusloyalty');
  }
  
  if (readCheckbox('#daybreak') || readCheckbox('#pegasus')) {
    showThese.push('treachery');
    hideThese.push('notreachery');
  } else {
    showThese.push('notreachery');
    hideThese.push('treachery');
  }
  
  if (readCheckbox('#cylonleader') || readCheckbox('#sympatheticcylon')) {
    showThese.push('infiltrator');
    hideThese.push('noinfiltrator');
    if (readCheckbox('#daybreak') || readCheckbox('#forcemotive')) {
      showThese.push('motive');
      hideThese.push('agenda');
    } else {
      showThese.push('agenda');
      hideThese.push('motive');
    }
  } else {
    showThese.push('noinfiltrator');
    hideThese.push('infiltrator');
    hideThese.push('agenda');
    hideThese.push('motive');
  }

  
  if (readCheckbox('#ioniannebula') 
       || readCheckbox('#allendings')
       || readCheckbox('#allyseasons')) {
    showThese.push('allies');
    hideThese.push('noallies');
  } else {
    showThese.push('noallies');
    hideThese.push('allies');
  }
  
  if (readCheckbox('#pegasus') || readCheckbox('#daybreak')
      || readCheckbox('#sympatheticcylon')
      || readCheckbox('#forceoverlay')) {
    showThese.push('overlay');
    hideThese.push('nooverlay');  
  } else {
    showThese.push('nooverlay');
    hideThese.push('overlay');
  }
  
  if (readCheckbox('#searchforhome')
        || readCheckbox('#forcedemetrius')
        || readCheckbox('#allendings')) {
    showThese.push('demetrius');
    hideThese.push('nodemetrius');
  } else {
    showThese.push('nodemetrius');
    hideThese.push('demetrius');
  }
  
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
    <label><input type="checkbox" name="wonderpack" id="wonderpack"> Wonder Pack</label><br>
    <label><input type="checkbox" name="catan" id="catan"> Catan Wonder</label><br>
    <hr>
    <label><input type="checkbox" name="leaders" id="leaders"> Leaders</label><br>
    <div style="margin-left: 20px" class="leaders">
        <label><input type="checkbox" name="leaders-anniversary">Leaders Anniversary Pack</label>
    </div>
    <label><input type="checkbox" name="cities" id="cities"> Cities</label><br>
    <div style="margin-left: 20px" class="cities">
        <label><input type="checkbox" name="cities-anniversary">Cities Anniversary Pack</label>
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
