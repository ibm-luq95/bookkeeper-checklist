"use strict";

import { showMicroModal } from "../../utils/model-box.js";

document.addEventListener("DOMContentLoaded", (ev) => {
  /*
    the browser fully loaded HTML, and the DOM tree is built, but external resources like pictures <img> and stylesheets may not yet have loaded.
    */
  const managerAddTaskBtn = document.querySelector("button#managerAddTaskBtn");
  const taskViewBtn = document.querySelectorAll("button.taskViewBtn");
  const taskDeleteBtn = document.querySelectorAll("button.taskDeleteBtn");
  const clientsTable = $("#managerJobTasksTable").DataTable({
    autoWidth: true,
    processing: true,
    // "info": false,
    // "paging": false,
    // stateSave: true,
    stateSaveCallback: function (settings, data) {
      localStorage.setItem("DataTables_" + settings.sInstance, JSON.stringify(data));
    },
    stateLoadCallback: function (settings) {
      return JSON.parse(localStorage.getItem("DataTables_" + settings.sInstance));
    },
    fixedHeader: true,
    responsive: true,
    dom: "Bfrtip",
    buttons: [
      // "copy",
      "csv",
      "pdf",
    ],
  });

  managerAddTaskBtn.addEventListener("click", (ev) => {
    showMicroModal("tasks-form-modal");
  });

  taskViewBtn.forEach(btn => {
    btn.addEventListener("click", (ev) => {
       const currentTarget = ev.currentTarget;
       const taskId = currentTarget.dataset["taskId"];
        alert(taskId);
    });
  });
  taskDeleteBtn.forEach(btn => {
    btn.addEventListener("click", (ev) => {
        const currentTarget = ev.currentTarget;
        const taskId = currentTarget.dataset["taskId"];
        alert(taskId);
    });
  });
});
