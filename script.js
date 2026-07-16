document.addEventListener("DOMContentLoaded", () => {
    document.querySelectorAll(".navbar a").forEach((link) => {
        link.addEventListener("click", (event) => {
            event.preventDefault();
            const target = document.querySelector(link.getAttribute("href"));

            if (target) {
                target.scrollIntoView({ behavior: "smooth" });
            }
        });
    });

    const profileForm = document.getElementById("profileForm");
    const createProfileBtn = document.getElementById("createProfileBtn");
    const profileDisplay = document.getElementById("profileDisplay");

    function createProfile() {
        const name = document.getElementById("studentName").value.trim();
        const roll = document.getElementById("rollNumber").value.trim();
        const branch = document.getElementById("branch").value.trim();
        const year = document.getElementById("year").value.trim();
        const goal = document.getElementById("careerGoal").value.trim();

        if (!name || !roll) {
            alert("Please enter at least your name and roll number");
            return;
        }

        profileDisplay.innerHTML = `
            <article class="task-item">
                <div>
                    <h3>${name} (${roll})</h3>
                    <p>${branch || "Branch not added"} - Year ${year || "not added"}</p>
                    <p>Goal: ${goal || "Not added"}</p>
                </div>
            </article>
        `;

        profileForm.reset();
    }

    createProfileBtn.addEventListener("click", createProfile);

    const addTaskBtn = document.getElementById("addTaskBtn");
    const taskList = document.getElementById("taskList");

    function toggleTaskStatus(badge) {
        if (badge.classList.contains("pending")) {
            badge.classList.remove("pending");
            badge.classList.add("complete");
            badge.textContent = "Completed";
        } else {
            badge.classList.remove("complete");
            badge.classList.add("pending");
            badge.textContent = "Pending";
        }
    }

    function addTask() {
        const titleInput = document.getElementById("taskTitle");
        const dateInput = document.getElementById("taskDueDate");
        const title = titleInput.value.trim();
        const date = dateInput.value;

        if (!title || !date) {
            alert("Please enter task title and due date");
            return;
        }

        const taskCard = document.createElement("article");
        taskCard.className = "task-item";
        taskCard.innerHTML = `
            <div>
                <h3>${title}</h3>
                <p>Due Date: ${date}</p>
            </div>
            <span class="badge pending">Pending</span>
        `;

        const badge = taskCard.querySelector(".badge");
        badge.addEventListener("click", () => toggleTaskStatus(badge));

        taskList.appendChild(taskCard);
        titleInput.value = "";
        dateInput.value = "";
    }

    addTaskBtn.addEventListener("click", addTask);

    document.querySelectorAll("#taskList .badge").forEach((badge) => {
        badge.addEventListener("click", () => toggleTaskStatus(badge));
    });

    const addProblemBtn = document.getElementById("addProblemBtn");
    const problemTableBody = document.getElementById("problemTableBody");

    function addProblem() {
        const titleInput = document.getElementById("problemTitle");
        const platformInput = document.getElementById("platformInput");
        const title = titleInput.value.trim();
        const platform = platformInput.value.trim();
        const difficulty = document.getElementById("difficultySelect").value;
        const status = document.getElementById("statusSelect").value;

        if (!title || !platform) {
            alert("Please enter problem title and platform");
            return;
        }

        const row = document.createElement("tr");
        row.innerHTML = `
            <td>${title}</td>
            <td>${platform}</td>
            <td>${difficulty}</td>
            <td>${status}</td>
        `;

        problemTableBody.appendChild(row);
        titleInput.value = "";
        platformInput.value = "";
    }

    addProblemBtn.addEventListener("click", addProblem);
});
