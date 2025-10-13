---
layout: page
title: Dynamic 7 Wonders rulebook
toc: true
toc_stop_autofire: true
---

<script type="text/javascript">
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
  return $(id).is(':checked');
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

</script>

<form id="configform" style="display: none;">
  <fieldset id="configbox">
    <legend>Configuration:</legend>
    <label><input type="checkbox" name="leaders" id="leaders"> Leaders</label>
    <label><input type="checkbox" name="leaders" id="leaders7"> Leaders Anniversary</label>
    <label><input type="checkbox" name="cities" id="cities"> Cities</label>
    <label><input type="checkbox" name="cities7" id="cities"> Cities Anniversary</label>

  </fieldset>
</form>

<div class="help" markdown="1">
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
<li>Each player selects or randomly gets a Wonder Board. Choose or select randomly <span class="1e">an A </span><span class="2e">a day </span>or <span class="1e">B </span><span class="2e">night </span> side. </li>
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
        <li><span class="armada babel">
        Choose between:
            <ul>
            <li class="armada"> If the card color matches Red, Yellow, Blue, or Green, you may pay the cost and move the corresponding boat on your shipyard board and apply the corresponding effect. If the effect is exploring an island, if you are the only one exploring that level's island, draw 4 cards and choose one to keep, returning the rest to the deck and shuffle. If multiple players are exploring the same level's island, they are dealt evenly all the cards from that level in the island deck, returning those cards that cannot be dealt. Each player choose which island to explore and return the rest to the deck, and shuffle. Place the island card under the Shipyard board on the corresponding space, leaving visible only the benefit granted. </li>
            <li class="babel greatprojects">If the card you constructed matches the color of the active Great Project, and there are available participation to-kens on the Great Project card, you can participate in its construction paying the Participation Cost. If you choose to do so, take a participation token and place it on your Wonder Board. </li>
            </ul>
        </li></ul>
    <li><p>Construct a stage of your wonder:</p>
        <p>Construct your wonder in order. <span class="armada">Siracusa stages can be built in any order. </span><span class="wonderpack">The Great Wall stages can be built in any order. </span></p>
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
Continue until you have 2 cards in your hand. If that's the case, discard one, and play the other one.

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