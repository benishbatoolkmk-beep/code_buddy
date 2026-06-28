/* =========================================================
   SECTION 1: SELECTING ELEMENTS
   ========================================================= */
 
const title = document.getElementById("mainTitle");
const para1 = document.querySelector("#para1");

console.log("Title element:", title);
console.log("Para element:", para1);
//title.style.color = "red";
//para1.textContent = para1.textContent + " - Yeh JS ne add kiya!";
 
/* =========================================================
   SECTION 2: CHANGING CONTENT
   ========================================================= */
 
const nameDisplay = document.getElementById("nameDisplay");
const nameInput = document.getElementById("nameInput");
const changeNameBtn = document.getElementById("changeNameBtn");
 

changeNameBtn.addEventListener("click", function () {
  const typedName = nameInput.value; 

/*if (typedName.trim() === "") {
    nameDisplay.textContent = "(Aap ne kuch nahi likha)";
  } else {
    nameDisplay.textContent = typedName;  
  } */
 nameDisplay.textContent = typedName.trim() === "" ? "(Aap ne kuch nahi likha)" : typedName;
});
 
 
/* =========================================================
   SECTION 3: CHANGING STYLE / CLASSLIST
   ========================================================= */
 
const colorText = document.getElementById("colorText");
const toggleHighlightBtn = document.getElementById("toggleHighlightBtn");
 
toggleHighlightBtn.addEventListener("click", function () {
  // classList.toggle: agar class lagi hai to hata do, nahi hai to laga do
colorText.classList.toggle("highlight");
 
});

 

// colorText.style.color = "red";
// colorText.style.fontWeight = "bold";
 
 
/* =========================================================
   SECTION 4: EVENTS - CLICK COUNTER

   ========================================================= */
 
const counterDisplay = document.getElementById("counterDisplay");
const counterBtn = document.getElementById("counterBtn");
let clickCount = 0; // yeh variable counter ki current value yaad rakhta hai

counterBtn.addEventListener("click", function () {
  clickCount = clickCount + 1;
 counterDisplay.textContent = clickCount;
});
 
 
/* =========================================================
   SECTION 5: ADDING / REMOVING ELEMENTS DYNAMICALLY

   ========================================================= */
 
const taskInput = document.getElementById("taskInput");
const addTaskBtn = document.getElementById("addTaskBtn");
const taskList = document.getElementById("taskList");
 
addTaskBtn.addEventListener("click", function () {
  const taskText = taskInput.value.trim();
  if (taskText === "") return; // khaali ho to kuch na karen
 
  // Step 1: naya <li> element
  const newLi = document.createElement("li");
  newLi.textContent = taskText;
 
  // Step 2: ek "Remove" button 
  const removeBtn = document.createElement("button");
  removeBtn.textContent = "X";
  removeBtn.style.marginLeft = "10px";
 
  // Jab Remove button click ho, parent <li> ko hata den
  removeBtn.addEventListener("click", function () {
    newLi.remove();
  });
 
  
  newLi.append(removeBtn);
  taskList.append(newLi);
 
  
  taskInput.value = "";
});
 