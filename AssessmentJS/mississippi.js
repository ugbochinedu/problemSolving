let word = "Mississippi";

function countSandI(word) {
  let countOfS = 0;
  let countOfI = 0;
  for (let index = 0; index < word.length; index++) {
    if (word[index] === "s") countOfS++;
    if (word[index] === "i") countOfI++;
  }
  console.log(
    "The number of s in mississippi is: " + countOfS +
      "\nThe number of i in mississippi is: " + countOfI
  );
}

countSandI(word);
