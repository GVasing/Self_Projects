// Global counter
let counter = 0 

// Global variables
let currentItemId = null;

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

const addButton = document.getElementById("addBtn");
const newItem = document.getElementById("toDoItem");

const allListContainers = document.getElementsByClassName("list_container");

const renamedItemToDo = document.getElementById("renameInputToDo");
const renamedItemInProgress = document.getElementById("renameInputInProg");
const renamedItemCompleted = document.getElementById("renameInputComp");

// This is a collection because there are multiple
const allLabelContainers = document.getElementsByClassName("container");

// This is a collection because there are multiple
const optionsMenuButtons = document.getElementsByClassName("options");

const optionButtons = document.getElementsByClassName("optionBtn");
const optionsMenuContainer = document.getElementsByClassName("optionsContainer");

// Options Menu Buttons for 'To Do' section
const renameButton = document.getElementById("renameButton");
const deleteButton = document.getElementById("deleteButton");
const moveToInProgressButton = document.getElementById("moveInProgressButton");
const moveToCompletedButton = document.getElementById("moveCompletedButton");

// Options Menu Buttons for 'In Progress' section
const renameButtonInProg = document.getElementById("renameButtonInProg");
const deleteButtonInProg = document.getElementById("deleteButtonInProg");
const moveToToDoButtonInProg = document.getElementById("moveToDoButtonInProg");
const moveToCompletedButtonInProg = document.getElementById("moveCompButtonInProg");

// Options Menu Buttons for 'Completed' section
const renameButtonComp = document.getElementById("renameButtonComp");
const deleteButtonComp = document.getElementById("deleteButtonComp");
const moveToToDoButtonComp = document.getElementById("moveToDoButtonComp");
const moveToInProgressButtonComp = document.getElementById("moveInProgButtonComp");

// Collection because there are multiple
const closeButtons = document.getElementsByClassName("closebutton");

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

function resetTextBoxValue(){
    newItem.value = "";
    renamedItemToDo.value = "";
    renamedItemInProgress.value = "";
    renamedItemCompleted.value = "";
}

// function optionsOverlayClose(){
//     const optionsOverlay = document.getElementsByClassName("optionsOverlay");
//     for (const overlay of optionsOverlay){
//         // overlay.style.opacity = "0";
//         // overlay.style.pointerEvents = "none";
//     };
// }

function createNewListItem(){
    // Get text value
    const itemValue = newItem.value;

    // Create elements and attributes required
    const newItemLabel = document.createElement("label");
    newItemLabel.className = "container";
    const newItemInput = document.createElement("input");
    newItemInput.type = "checkbox";
    const newItemSpan = document.createElement("span");
    newItemSpan.className = "checkmark";
    const newItemMenuButton = document.createElement("button");
    newItemMenuButton.className = "options";
    newItemMenuButton.id = "item-" + counter;
    const newItemButtonLink = document.createElement("a");
    newItemButtonLink.href = "#OptionsToDo";

    // Get parent container
    const listContainer = document.getElementById("toDoListContainer");

    // Add label to parent container
    listContainer.appendChild(newItemLabel);

    // Add elements to label
    newItemLabel.appendChild(newItemInput);
    newItemLabel.appendChild(newItemSpan);
    newItemLabel.appendChild(newItemButtonLink);

    // Get and add textbox value to label
    const newItemValue = document.createTextNode(itemValue);
    newItemLabel.appendChild(newItemValue);

    // Add button to anchor element
    newItemButtonLink.appendChild(newItemMenuButton);

    // Create values for buttons and add to them
    const buttonValue = document.createTextNode("⁝");
    newItemMenuButton.appendChild(buttonValue);

    // Increment counter
    counter ++;

    // Loop through each options button and add an event listener
    for (const menuButton of optionsMenuButtons){
        console.log(menuButton);
        menuButton.addEventListener("click", retrieveElementId);
    };

    // Reset textbox
    resetTextBoxValue();
}

function moveListItemToInProgress(){
    // Get item value
    const itemToMove = document.getElementById(currentItemId);
    const parentContainer = itemToMove.parentElement;  
    const grandparentContainer = parentContainer.parentElement;

    // Change link/href for tricolon
    parentContainer.href = "#OptionsInProgress";

    // Get parent container
    const listContainer = document.getElementById("inProgressListContainer");

    // Add item to container
    listContainer.appendChild(grandparentContainer);

    // Loop through each options button and add an event listener
    for (const menuButton of optionsMenuButtons){
        console.log(menuButton);
        menuButton.addEventListener("click", retrieveElementId);
    };

    // Change overlay opacity
    // optionsOverlayClose();
}

function moveListItemToCompleted(){
    // Get item value
    const itemToMove = document.getElementById(currentItemId);
    const parentContainer = itemToMove.parentElement;
    const grandparentContainer = parentContainer.parentElement;

    // Change link/href for tricolon
    parentContainer.href = "#OptionsComplete";

    // Get parent container
    const listContainer = document.getElementById("completedListContainer");

    // Add item to container
    listContainer.appendChild(grandparentContainer);

    // Loop through each options button and add an event listener
    for (const menuButton of optionsMenuButtons){
        console.log(menuButton);
        menuButton.addEventListener("click", retrieveElementId);
    };

    // Change overlay opacity
    // optionsOverlayClose();
}

function moveListItemToToDo(){
    // Get item value
    const itemToMove = document.getElementById(currentItemId);
    const parentContainer = itemToMove.parentElement;
    const grandparentContainer = parentContainer.parentElement;

    // Change link/href for tricolon
    parentContainer.href = "#OptionsToDo";

    // Get parent container
    const listContainer = document.getElementById("toDoListContainer");

    // Add item to container
    listContainer.appendChild(grandparentContainer);

    // Loop through each options button and add an event listener
    for (const menuButton of optionsMenuButtons){
        console.log(menuButton);
        menuButton.addEventListener("click", retrieveElementId);
    };

    // Change overlay opacity
    // optionsOverlayClose();
}

function addListItems(event){
    if (event.type === "click"){
        createNewListItem();
    } else if (event.type === "keypress"){
        if (event.key === "Enter"){
            createNewListItem();
        }
    }
}

function retrieveElementId(event) {
    const clickedElement = event.target;
    const buttonId = clickedElement.getAttribute('id');
    currentItemId = buttonId;
    console.log(currentItemId);
}

function renameItemToDo(){
    const newName = renamedItemToDo.value;
    const itemToRename = document.getElementById(currentItemId);
    const parentContainer = itemToRename.parentElement;
    const grandparentContainer = parentContainer.parentElement;
    for (const child of grandparentContainer.childNodes){
        if (child.nodeType === Node.TEXT_NODE){
            child.nodeValue = newName;
            console.log(child.nodeValue);
        };
    };
    // Reset textbox
    resetTextBoxValue();

    // Change overlay opacity
    // optionsOverlayClose();
}

function renameItemInProg(){
    const newName = renamedItemInProgress.value;
    const itemToRename = document.getElementById(currentItemId);
    const parentContainer = itemToRename.parentElement;
    const grandparentContainer = parentContainer.parentElement;
    for (const child of grandparentContainer.childNodes){
        if (child.nodeType === Node.TEXT_NODE){
            child.nodeValue = newName;
            console.log(child.nodeValue);
        };
    };
    // Reset textbox
    resetTextBoxValue();

    // Change overlay opacity
    // optionsOverlayClose();
}

function renameItemComp(){
    const newName = renamedItemCompleted.value;
    const itemToRename = document.getElementById(currentItemId);
    const parentContainer = itemToRename.parentElement;
    const grandparentContainer = parentContainer.parentElement;
    for (const child of grandparentContainer.childNodes){
        if (child.nodeType === Node.TEXT_NODE){
            child.nodeValue = newName;
            console.log(child.nodeValue);
        };
    };
    // Reset textbox
    resetTextBoxValue();

    // Change overlay opacity
    // optionsOverlayClose();
}

function deleteItem(){
    // Access item by global variable 
    const itemToDelete = document.getElementById(currentItemId);

    // Track back to grandparent container
    const parentContainer = itemToDelete.parentElement;
    const grandparentContainer = parentContainer.parentElement;

    // Remove container
    grandparentContainer.remove();

    // Change overlay opacity
    // optionsOverlayClose();
}

addButton.addEventListener("click", addListItems);
newItem.addEventListener("keypress", addListItems);

// Event Listener for closing overlay with 'esc'
document.addEventListener("keydown", (event) => {
    if (event.key === "Escape"){
        for (const closeButton of closeButtons){
            const parentDiv = closeButton.parentElement;
            if (window.location.hash === `#${parentDiv.id}`){
                closeButton.click();
                break;
            } 
        };
    };
});

// Event Listeners for 'To Do' section option buttons
renameButton.addEventListener("click", renameItemToDo);
deleteButton.addEventListener("click", deleteItem);
moveToInProgressButton.addEventListener("click", moveListItemToInProgress);
moveToCompletedButton.addEventListener("click", moveListItemToCompleted);

// Event Listeners for 'In Progress' section option buttons
renameButtonInProg.addEventListener("click", renameItemInProg);
deleteButtonInProg.addEventListener("click", deleteItem);
moveToToDoButtonInProg.addEventListener("click", moveListItemToToDo);
moveToCompletedButtonInProg.addEventListener("click", moveListItemToCompleted);

// Event Listeners for 'Completed' section option buttons
renameButtonComp.addEventListener("click", renameItemComp);
deleteButtonComp.addEventListener("click", deleteItem);
moveToToDoButtonComp.addEventListener("click", moveListItemToToDo);
moveToInProgressButtonComp.addEventListener("click", moveListItemToInProgress);


// click on button (class=options) and .optionsOverlay opacity should change to 1.

// const itemToRename = document.getElementById(currentItemId);
// const parentContainer = itemToRename.parentElement;
// const grandparentContainer = parentContainer.parentElement;
// console.log(grandparentContainer);
// for (const child of grandparentContainer.childNodes){
//     if (child.nodeType === Node.TEXT_NODE){
//         const containerText = child.nodeValue;            
//         console.log(containerText);
//         return containerText;
//     };
// };

// optionsMenuButton.addEventListener("click", function(){
//     const optionsMenuOverlay = document.getElementsByClassName("optionsOverlay");
//     optionsMenuOverlay.style.opacity = "1";
// })

// optionsMenuButton.addEventListener("click", function(){
//     const optionMenuContainer = document.getElementsByClassName("optionsContainer");
//     optionMenuContainer.style.display = ""
// })

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