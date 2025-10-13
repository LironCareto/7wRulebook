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
      <label><input type="radio" name="edition" id="Ed1" /> 1st Edition</label>
      <label><input type="radio" name="edition" id="Ed2" /> 2nd Edition</label>
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
    <label><input type="radio" name="babeledifice" id="babel"> Babel</label><br>
    <div style="margin-left: 20px" class="babel">
        <label><input type="checkbox" name="tower" id="tower"> Babel Tower</label>
        <label><input type="checkbox" name="greatprojects" id="greatprojects"> Babel Great Projects</label>
    </div>
    <label><input type="radio" name="babeledifice" id="edifice"> Edifice</label><br>
    <label><input type="checkbox" name="armada" id="armada"> Armada</label><br>
    <div style="margin-left: 20px" class="siracusa">
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


<div class="help" markdown="1">
## Help

Use the checkboxes and menus above to select a configuration of Battlestar Galactica expansions, modules, and variants. Some items might be disabled if they conflict with another selected option. 

### All endings

Many variants exist that add *all* the endings to the game. None of them are included here, but you can still use this rulebook for such a game by selecting "all endings". This will show all of the official rules for every ending. Whichever variant you are using will tell you how to proceed through all the endings, but when you need to resolve "normal" gameplay events and issues they will be available.

### Agendas and Motives

Pegasus and Daybreak both added Cylon Leaders, but the way that Cylon Leaders win is different in Daybreak. You can choose to "backport" Motive cards to the Pegasus elements that use Agenda cards (Cylon Leaders and Sympathetic Cylon). The reverse (using Agenda cards in Daybreak for Cylon Leaders) isn't integrated into the rules, because Agenda cards are very simple and don't have any rule conflicts. All you have to do is:

- Give the Cylon Leader a Hostile (for a 5 or 7 player game) or Sympathetic (4 or 6 player game) Agenda card when the first round of Loyalty cards goes out.
- Ignore any mention of Motive cards in the rules. 
- Use the text of the Agenda card to determine whether the Cylon Leader wins or loses at the end of the game. 

### Sympathizer variants

The "Sympathizer" role from the base game is intended to be a sort of "half-Cylon": if the game is going well for the humans, a new Cylon is added (with some restrictions), but if not, a human player is merely sent to the Brig. 

This card proved to be rather unpopular for a few reasons. For one, the unlucky player who becomes a Cylon via the Sympathizer card is immediately revealed as a Cylon and doesn't get to secretly sabotage the humans, and even as a Cylon they do not get a Super Crisis and cannot use the Cylon Fleet location, removing over a quarter of their possible Cylon actions. Secondly, it adds an incentive for the humans to sabotage themselves before the Sleeper Agent phase so that the Sympathizer stays human. 

There are a few options for avoiding the Sympathizer. Daybreak and Pegasus add Cylon Leaders, special characters who are almost literally half-Cylons and therefore remove the need for a Sympathizer when they are used. Pegasus adds the option of using the "Sympathetic Cylon" Loyalty card, which is very similar to the Sympathizer but instead changes a player into essentially a Cylon Leader. As a variant, you can even choose to just use the Sympathetic Cylon without the rest of Pegasus. 

Daybreak replaces both the "Sympathizer" and "Sympathetic Cylon" with "The Mutineer", a player who gets lots of Mutiny cards, so no variant is necessary to avoid the Sympathizer using this expansion. 

The simplest option, however, requiring no expansions at all, is the "No Sympathizer" variant which was officially released by Fantasy Flight Games. It just handicaps the humans and allows Cylons to draw more cards. 

### Allies for All Seasons

This variant was designed by Alexander DeSouza. It allows the "Ally" mechanic to be added to a game without having to use the entire Ionian Nebula ending. 

### Loyalty deck variants

The Loyalty deck variants have to do with the Exodus "extra card" rule change. In Pegasus, an executed human player always comes back as a human. This is a little unfortunate from a story perspective: the humans can perform a rather gruesome, but guaranteed, Cylon test for a relatively small cost. Exodus changes this, and always leaves an extra Loyalty card in the deck. This has two effects: an executed human may come back as a Cylon, but a Cylon card might remain in the deck, never dealt to a player at all. 

Both have their pros and cons. The Pegasus version has the advantage that the game is never short a Cylon. The Exodus version has more intrigue, and avoids giving the humans a perverse incentive to kill their own teammates. The Exodus version starts to make even more sense when Personal Goal and Final Five cards are included, because even if an executed human comes back as a human, they may be stuck with one of these human-hostile cards. The Pegasus version starts to make more sense with fewer players, since it becomes more likely that the remaining card will be a Cylon. 

Some game mechanics depend on the Exodus version, like Personal Goal cards and some Ally cards. When those are enabled, you will be forced to use the Exodus style. Otherwise, you can choose whichever one you like best: guaranteed Cylons but also an easy test, or more uncertainty and the possibility of a missing Cylon. You could also pick one, but add an additional rule to mitigate the downsides. Some examples include:

- Exodus rules, then at distance 7, all human players roll the die. The lowest receives the final Loyalty card, guaranteeing that the last Cylon gets out at some point.
- Pegasus rules, but a new human character must draw from a special deck that is half “Personal Goal”/”Final Five” cards, half normal “Not A Cylon” cards. They’ll still be a guaranteed human, but dealing with the special Loyalty card can penalize the humans for killing an innocent.
- Exodus rules, then at the end of the game, if the remaining card was a Cylon, deduct 1 from each resource as a handicap before declaring a human victory.

</div>


{% include toc.html %}

<div id="statictoc" class="nojs">
<i>Jump to...</i> <ol><li><a href="#introduction">Introduction</a></li><li><a href="#the-basics">The basics</a><ol><li><a href="#strategy">Strategy</a></li></ol></li><li><a href="#game-setup">Game setup</a><ol><li><a href="#game-board">Game board</a></li><li><a href="#pegasus">Pegasus</a></li><li><a href="#exodus">Exodus</a></li><li><a href="#daybreak">Daybreak</a></li><li><a href="#kobol-ending">Kobol ending</a></li><li><a href="#new-caprica-ending">New Caprica ending</a></li><li><a href="#ionian-nebula-ending">Ionian Nebula ending</a></li><li><a href="#search-for-home-ending">Search for Home ending</a></li><li><a href="#choosing-characters">Choosing characters</a></li><li><a href="#loyalty-deck">Loyalty Deck</a></li><li><a href="#first-hand-of-cards">First hand of cards</a></li><li><a href="#ionian-nebula-additional-setup">Ionian Nebula additional setup</a></li><li><a href="#rule-reminders">Rule reminders</a></li></ol></li><li><a href="#playing-the-game">Playing The Game</a><ol><li><a href="#game-turn">Game turn</a></li><li><a href="#player-terminology">Player terminology</a></li><li><a href="#secrecy">Secrecy</a></li><li><a href="#resolving-rule-conflicts">Resolving rule conflicts</a></li><li><a href="#component-limitations">Component limitations</a></li><li><a href="#die-rolls">Die rolls</a></li><li><a href="#timing">Timing</a></li><li><a href="#resources">Resources</a></li><li><a href="#trauma-tokens">Trauma Tokens</a><ol><li><a href="#trauma-tokens-on-locations">Trauma tokens on locations</a></li></ol></li><li><a href="#ally-cards">Ally cards</a><ol><li><a href="#placing-a-new-ally">Placing a new Ally</a></li><li><a href="#ally-replaced-with-player-or-location-damaged">Ally replaced with player, or location damaged</a></li></ol></li><li><a href="#demetrius--missions">Demetrius &amp; Missions</a></li><li><a href="#rebel-basestar-human-or-cylon">Rebel Basestar (human or Cylon)</a></li><li><a href="#character-sheets">Character sheets</a></li><li><a href="#once-per-game">Once per game</a></li><li><a href="#loyalty-cards">Loyalty cards</a><ol><li><a href="#personal-goal-cards">Personal Goal cards</a></li><li><a href="#final-five-cards">Final Five cards</a></li><li><a href="#the-mutineer">The Mutineer</a></li></ol></li><li><a href="#mutiny-cards">Mutiny cards</a><ol><li><a href="#drawing-a-second-mutiny-card">Drawing a second Mutiny card</a></li><li><a href="#discarding-treachery-cards-and-gaining-mutiny-cards">Discarding Treachery cards and gaining Mutiny cards</a></li></ol></li><li><a href="#cylon-players">Cylon Players</a><ol><li><a href="#cylon-reveal-resolution">Cylon Reveal resolution</a></li></ol></li><li><a href="#titles">Titles</a><ol><li><a href="#president">President</a></li><li><a href="#admiral">Admiral</a></li><li><a href="#cag-commander-air-group">CAG (Commander, Air Group)</a></li></ol></li><li><a href="#lines-of-succession">Lines of Succession</a></li><li><a href="#actions--abilities">Actions &amp; Abilities</a><ol><li><a href="#movement-actions">Movement actions</a></li></ol></li><li><a href="#moves">Moves</a><ol><li><a href="#sabotage-treachery-card-interrupt">“Sabotage” Treachery card interrupt</a></li><li><a href="#moves-versus-movement-actions">Moves versus Movement actions</a></li></ol></li><li><a href="#skill-cards">Skill Cards</a><ol><li><a href="#skill-check-abilities">Skill Check Abilities</a></li><li><a href="#reckless-cards-and-abilities">Reckless cards and abilities</a></li><li><a href="#types">Types</a></li><li><a href="#destiny-deck">Destiny Deck</a></li></ol></li><li><a href="#crisis-card-resolution">Crisis card resolution</a></li><li><a href="#event-crisis-cards">Event Crisis cards</a></li><li><a href="#super-crisis-cards">Super Crisis Cards</a></li><li><a href="#skill-check-resolution">Skill Check resolution</a></li><li><a href="#activating-cylon-ships">Activating Cylon ships</a><ol><li><a href="#activating-a-raider">Activating a raider</a></li><li><a href="#activating-heavy-raiders-and-centurions">Activating heavy raiders and Centurions</a></li></ol></li><li><a href="#jumping-the-fleet">Jumping the fleet</a></li><li><a href="#sleeper-agent-phase">Sleeper Agent phase</a><ol><li><a href="#revealed-cylons-during-the-sleeper-agent-phase">Revealed Cylons during the Sleeper Agent phase</a></li></ol></li><li><a href="#combat-ship-attack-table">Combat ship attack table</a><ol><li><a href="#basestar-damage">Basestar damage</a></li><li><a href="#damaging-galactica">Damaging Galactica</a></li><li><a href="#damaging-pegasus">Damaging Pegasus</a></li><li><a href="#scar">Scar</a></li></ol></li><li><a href="#human-combat-ships">Human combat ships</a><ol><li><a href="#civilian-ships">Civilian ships</a><ol><li><a href="#drawing-and-destroying">Drawing and destroying</a></li></ol></li><li><a href="#raptors">Raptors</a></li><li><a href="#vipers">Vipers</a></li><li><a href="#mark-vii-vipers">Mark VII Vipers</a></li><li><a href="#assault-raptors">Assault raptors</a></li><li><a href="#piloting">Piloting</a></li></ol></li><li><a href="#execution">Execution</a><ol><li><a href="#finishing-a-cylon-execution">Finishing a Cylon execution</a></li><li><a href="#finishing-a-human-execution">Finishing a human execution</a></li></ol></li><li><a href="#character-ability-notes">Character ability notes</a></li><li><a href="#location-notes">Location notes</a><ol><li><a href="#commmand">Commmand</a></li><li><a href="#the-brig">The Brig</a></li><li><a href="#choosing-players-for-sickbaybrig">Choosing players for Sickbay/Brig</a></li><li><a href="#colonial-one">Colonial One</a></li><li><a href="#cylon-fleet-location">Cylon Fleet location</a></li><li><a href="#basestar-bridge">Basestar Bridge</a></li></ol></li></ol></li><li><a href="#ending-the-game">Ending the game</a><ol><li><a href="#new-caprica-phase">New Caprica phase</a><ol><li><a href="#new-caprica-phase-setup">New Caprica phase setup</a></li><li><a href="#new-caprica-phase-rules">New Caprica phase rules</a><ol><li><a href="#occupation-forces">Occupation Forces</a></li><li><a href="#preparing-civilian-ships">Preparing civilian ships</a></li><li><a href="#brig-versus-detention">Brig versus Detention</a></li></ol></li><li><a href="#before-galactica-returns">Before Galactica returns</a></li><li><a href="#after-galactica-returns">After Galactica returns</a></li><li><a href="#evacuating-new-caprica">Evacuating New Caprica</a></li></ol></li><li><a href="#ionian-nebula-crossroads-phase">Ionian Nebula: Crossroads Phase</a><ol><li><a href="#battle-of-the-ionian-nebula">Battle of the Ionian Nebula</a></li><li><a href="#crossroads">Crossroads</a></li><li><a href="#the-trialboxing-the-line">The Trial/Boxing the Line</a></li><li><a href="#elimination">Elimination</a></li></ol></li><li><a href="#human-loss">Human loss</a></li><li><a href="#final-jump">Final jump</a></li></ol></li></ol>
</div>

## Introduction


## The basics


## Game setup
Prepare a spacious table.

<ol>
<li>Separate the Age cards into the three Age decks. </li>
<li>Discard the cards that show a player count above the number of players. </li>
<li class="cities">Separate the Black cards into the three Age decks and shuffle each. </li>
<li class="cities">For each age add as many black cards as there are players. </li>
<li>Shuffle all the purple (Guild) cards and draw the <em>number of players + 2 </em>and add them to the Age III deck. </li>
<li class="armada">Separate the Armada Age cards into the three age decks and shuffle each. </li>
<li class="armada">For each age, add as many Armada cards as there are players. </li>
<li>Add to the set of wonders <span class="cities">Byzantium, Petra, </span><span class="armada">Siracusa, </span><span class="leaders">Rome, Abu Simbel, </span><span class="edifice">Ur, </span>to the set of wonders. </li>
<li>Each player selects or randomly gets a Wonder Board. Choose or select randomly <span class="Ed1">an A </span><span class="Ed2">a day </span>or <span class="Ed1">B </span><span class="Ed2">night </span> side. </li>
<li>Each player gets <span class="no-leaders">3 </span><span class="leaders">6 </span>coins from the bank. </li>
<li class="babel tower">Place the base of the Babel Tower depending on the number of players (2-4 players, 3 placeholders; 5-8 players, 4 placeholders). </li>
<li class="babel tower">Deal 3 random Babel tiles in front of them, face down. </li>
<li class="babel tower">Secretly choose one tile, place it down in front of you and pass the remaining to the player on your right. </li>
<li class="babel tower">Repeat until each player receives the last tile from the player to the left and each player has 3 tiles in their pile. </li>
<li class="leaders">Deal 4 random leader cards to each player</li>
<li class="leaders">Secretly choose one leader card and place it face down in front of you. </li>
<li class="leaders">Pass the rest of the cards to the person on your right. </li>
<li class="leaders">Repeat until all the cards are used, so each person has a leader card in hand, which is discarded. </li>
<li class="armada">Each player gets a shipyard board and a boat of each color. </li>
<li class="armada">The island cards are added to the table in separate piles for each level. </li>
<li class="edifice">Separate the Edifice cards into the three Ages, shuffle them and place one random card per Age, project face up, in the middle of the table. </li>
<li class="edifice">Put the number of participation pawns (2,3,3,4,5) on each card depending on the number of players (3,4,5,6,7).
<div markdown="1">
| Players | Pawns |
| ------- | ----- |
|    3    |   2   |
|    4    |   3   |
|    5    |   3   |
|    6    |   4   |
|    7    |   5   |

</div>
</li>
</ol>

## Turn order
### Start of Age
<ol>
<li class="babel greatprojects">Take one Great Project card and place it in the middle of the table, and place on it as many Participation tokens as the number of players minus one. </li>
<li class="leaders">Choose one of your leader cards and place them face down in front of you.
You can:
<ul>
<li>Recruit this Leader:
    <ul>
    <li>Reveal the leader and pay its cost in coins. Place your leader face up next to your wonder. From now on you can benefit from its effect. </li>
    <li>If the cost shows 'A' then it cost in coins is the current Age. </li></ul>
<li>Construct a stage of your Wonder:
    <ul>
    <li>Use the leader card to build a stage of your wonder following the usual rules. </li></ul>
<li>Sell this leader:
    <ul>
    <li>Discard the leader card and take 3 coins from the bank. </li></ul>
</li>
<li>Choose a card from your hand, and pass the deck to the player of your left or right (look at the curved arrow on the back of the cards).
    <ul>
    <li>Construct the card <strong>as long as it's not already existing in your city</strong>:
        <ul>
        <li>Pay the cost shown on the card and place it, face up, behind your wonder. Resources must com from you or your neighbors. Each resource costs 2 coins. </li>
        <li><span class="armada babel greatprojects">Choose between:</span>
            <ul>
            <li class="armada"> If the card color matches Red, Yellow, Blue, or Green, you may pay the cost and move the corresponding boat on your shipyard board and apply the corresponding effect. If the effect is exploring an island, if you are the only one exploring that level's island, draw 4 cards and choose one to keep, returning the rest to the deck and shuffle. If multiple players are exploring the same level's island, they are dealt evenly all the cards from that level in the island deck, returning those cards that cannot be dealt. Each player choose which island to explore and return the rest to the deck, and shuffle. Place the island card under the Shipyard board on the corresponding space, leaving visible only the benefit granted. </li>
            <li class="babel greatprojects">If the card you constructed matches the color of the active Great Project, and there are available participation to-kens on the Great Project card, you can participate in its construction paying the Participation Cost. If you choose to do so, take a participation token and place it on your Wonder Board. </li>
            </ul>
        </li>
    <li>Construct a stage of your wonder:
        Construct the next stage of your wonder in order. <span class="siracusa">Siracusa stages can be built in any order. </span><span class="wonderpack">The Great Wall stages can be built in any order. </span>
        <ul>
        <li>Turn the card face down and pay the cost shown on the wonder space it is being used for. Place the upside-down card on the bottom of the wonder under the stage you have built. <span class="edifice">Once per age, when you construct a stage of your wonder you can participate in the construction in the current age's edifice. Pay the cost of your wonder stage and the project cost at the same time, then take a participation pawn from the card. If multiple players contribute on the same turn, take extra pawns from the box if needed. If all pawns are taken from the edifice card, then it is constructed. Flip the card over and anyone with a participation pawn immediately gains the reward shown on the card. <span class="armada">You cannot move a ship forward <strong>and </strong>contribute to a project on the same turn</span></span><span class="armada">Move a boat on your shipyard board on the column with the wonder symbol<span class="edifice"> only if you didn't participate in the edifice construction this turn</span>. </span></li></ul>        
    <li>Sell the card:
        <ul>
        <li>Discard the card face down in the middle of the table and take 3 coins from the bank<span class="armada"> <strong>or </strong>move your yellow boat up a row without paying the naval cost</span>. </li></ul>
    </li></ul>
    <li class="babel tower">Build the Babel Tower:
        <ul>
        <li>Discard the card and place the chosen Babel Tower tile face down in front of you. Once all players have played their turn, place your tile on the board, starting from the placeholder marked with the circular arrow. If more than one player is building the table, the tiles are placed in order of the number printed in the tile. </li>
        <li>The effects of the Babel Tower tiles apply to all players as long as they are not covered by another Babel Tower tile. </li></ul>
    </li>
</li>
<p>Continue until you have 2 cards in your hand. If that's the case, discard one, and play the other one.</p>

#### Turn Resolution
The turn is always resolved in this order
<ol>
<li>Pay all construction costs (card, Wonder<span class="armada">, Naval Construction</span>) </li>
<li class="armada">Move the Ship corresponding to your Naval Construction, if any. </li>
<li class="babel tower"></li>
<li>Apply all effects<span class="armada"> except Tax and Piracy</span>. </li>
<li class="armada">Resolve Island exploration. </li> 
<li>Resolve construction of cards from the discard pile<span class="armada"> (no Naval Construction allowed)</span>. </li>
<li class="armada">Resolve Tax and Piracy. </li>
</ol>

### End of Age
<ol>
<li class="babel greatprojects">Check the completion status of the Great Project
    <ul>
    <li><strong>The Great Project is a success. </strong> If all participation tokens have been taken all players who participated gain as many reward tokens as they have participation tokens in their possession. The return tokens are returned to the supply. </li>
    <li><strong>The Great Project is a failure. </strong>If there are remaining tokens on the Great Project card, those players without a participation token suffer the penalty displayed on the Great Project card. The return tokens are returned to the supply. </li>
    </ul>
    If a player cannot pay the penalty, they must take a penalty token for value according to the Age (-1, -2, or -3). 
</li>
<li>Resolve <span class="no-armada">Military</span><span class="armada">Ground</span> Conflict. Award bonus and penalty points comparing your <span class="no-armada">military strength</span><span class="armada">Ground Shields</span> to your left and right neighbors'<span class="armada"> and players you've given an incursion token to (diplomacy tokens do not affect boarding tokens)</span>. In case of tie no one gets a bonus/penalty token. <span class="cities">If you have a diplomacy token, you do not participate in military conflicts and your neighbors to your left and right compare each other as if they were adjacent. Discard the diplomacy token after the resolution of all conflicts. </span></li>
<li class="armada">Resolve Naval conflicts. Award bonus and penalty tokens. The comparison is done among all players. The weakest Naval Strength gets a penalty bonus, then the strongest, second and third get the corresponding bonuses, in that order. 
<div markdown="1">
|  Age  | Weakest | Strongest | 2nd Strongest | 3rd Strongest |
|  ---  | ------- | --------- | ------------- | ------------- |
|  I    |    -1   |     3     |       1       |               |
|  II   |    -2   |     5     |       3       |               |
|  III  |    -3   |     7     |       5       |       3       |

</div>
In case of a tie for the weakest, both players take a Naval Defeat token. In case of a tie for the strongest, both players take the reward of the next rank, and the second goes down to the third rank. In case of a tie in second strongest, both players go down to third rank and the player(s) in third position get no bonus tokens.
</li>

Each Guild Card is limited to a maximum of 10 points.