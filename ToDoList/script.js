// Get elements
const firstRightArrow = document.getElementById("homerightarrow");
const secondRightArrow = document.getElementById("toDoRightArrow");
const thirdRightArrow = document.getElementById("inProgressRightArrow");

const firstLeftArrow = document.getElementById("toDoLeftArrow");
const secondLeftArrow = document.getElementById("inProgressLeftArrow");
const thirdLeftArrow = document.getElementById("completeLeftArrow");

const home = document.getElementById("home");
const toDo = document.getElementById("todo");
const inProgress = document.getElementById("inprogress");
const completed = document.getElementById("completed");

function changePage(element, section){
    element.addEventListener("click", function(){
        section.scrollIntoView({behavior: "smooth", inline: "center"});
    })
}

changePage(firstRightArrow, toDo);
changePage(firstLeftArrow, home);
changePage(secondRightArrow, inProgress);
changePage(secondLeftArrow, toDo);
changePage(thirdRightArrow, completed);
changePage(thirdLeftArrow, inProgress);


// const sections = {
//     0: home,
//     1: toDo,
//     2: inProgress
// };

// // const leftArrows = document.getElementsByClassName("leftarrow")
// const leftArrows = document.querySelectorAll(".leftarrow");
// const rightArrow = document.getElementsByClassName("rightarrow")

// function goBackwards(sectionId){
//     leftArrows.forEach(item => {
//         item.addEventListener("click", function(){
//             const desiredSect = document.getElementById(`${sectionId}`);
//             desiredSect.scrollIntoView({behavior: "smooth", inline: "center"});
//         });
//     })
// }

// goBackwards("home");