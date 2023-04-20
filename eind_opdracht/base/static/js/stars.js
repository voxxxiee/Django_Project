/**
 * Functie om sterren te maken voor bij de leesacties.
 * Dit is nou 3 keer geschreven elke keer net iets anders dus misschien kijken
 * of dat allemaal via deze functie kan want dat zou wel cool zijn.
 * 
 * @return void
 */
function printStars() {
	var starsSpan = document.getElementById("stars");
	var score = document.getElementById("user_score");
	// clear de span bij elke verandering
	starsSpan.innerHTML = "";
	// loop voor het aantal sterren toevoegen
	for (var i = 0; i < parseInt(score.innerHTML); i++)
	{
		// maak een material icons ster aan en voeg die aan de span toe.
		var star = document.createElement("i");
		star.classList.add("material-icons");
		star.innerHTML = "star";
		starsSpan.appendChild(star);
	}
}
