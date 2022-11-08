"use strict";

import { getCookie } from "../../utils/cookie.js";
import { enableInputsOnLoad, sendRequest } from "../../utils/helpers.js";
import { showMicroModal } from "../../utils/model-box.js";
import { showToastNotification } from "../../utils/notifications.js";
document.addEventListener("readystatechange", (ev) => {
  // The document is still loading.
  /* if (document.readyState === "loading") {

    } */

  // The document has finished loading and the document has been parsed but sub-resources such as scripts, images, stylesheets and frames are still loading.
  /* if (document.readyState === "interactive") {

    } */

  // check if the page fully loaded with all resources
  if (document.readyState === "complete") {
    enableInputsOnLoad("bkchlst-input");
    const addNewJobBtn = document.querySelector("#addNewJobBtn");
    const addNewClientBtn = document.querySelector("#addNewClientBtn");
    const readonlySelectElements = document.querySelectorAll(".readonly-select");
    readonlySelectElements.forEach((element) => {
      element.addEventListener("change", (event) => {
        return false;
      });
    });
    $("#edit-preferences").click(function () {
      $("#edit-preferences-modal").addClass("is-active");
    });
    $(".modal-card-head button.delete, .modal-save, .modal-cancel").click(function () {
      $("#edit-preferences-modal").removeClass("is-active");
    });
    $("#tabs li").on("click", function () {
      const tab = $(this).data("tab");

      $("#tabs li").removeClass("is-active");
      $(this).addClass("is-active");

      $("#tab-content section").removeClass("is-active");
      $('section[data-content="' + tab + '"]').addClass("is-active");
    });

    if (addNewJobBtn) {
      addNewJobBtn.addEventListener("click", (event) => {
        showMicroModal("jobs-form-modal");
      });
    }
    if (addNewClientBtn) {
      addNewClientBtn.addEventListener("click", (event) => {
        showMicroModal("client-form-modal");
      });
    }
    $.fn.dataTable.ext.buttons.alert = {
      className: "buttons-alert",

      action: function (e, dt, node, config) {
        alert(this.text());
      },
    };
    const jobsTable = $("#managerClientsJobsTable").DataTable({
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
        {
          text: "Add New Job",
          className: "is-success",
          action: (e, dt, node, config) => {
            // console.log(config);
            // alert("Button activated");
            // dt.data.reload();
            showMicroModal("jobs-form-modal");
          },
        },
      ],
    });

    const clientsTable = $("#managerClientsTable").DataTable({
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
        {
          text: "Add New Client",
          className: "is-success",
          action: (e, dt, node, config) => {
            // console.log(config);
            // alert("Button activated");
            // dt.data.reload();
            showMicroModal("client-form-modal");
          },
        },
      ],
    });

    const tasksTable = $("#managerTasksTable").DataTable({
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
        {
          text: "Add New Task",
          className: "is-success",
          action: (e, dt, node, config) => {
            // console.log(config);
            // alert("Button activated");
            // dt.data.reload();
            showMicroModal("tasks-form-modal");
          },
        },
      ],
    });

    const managerAddNewJobForm = document.querySelector("#managerAddNewJobForm");
    managerAddNewJobForm.addEventListener("submit", (event) => {
      event.preventDefault();
      const currentTarget = event.currentTarget;
      const submitBtn = document.querySelector("button#managerAddNewJobBtn");
      submitBtn.disabled = true;
      submitBtn.classList.add(...["disabled", "cur-progress", "is-disabled"]);
      const formData = new FormData(currentTarget);
      const requestOptions = {
        method: "POST",
        dataToSend: formData,
        url: currentTarget.action,
      };
      const tasksArray = formData.getAll("tasks");
      formData.delete("tasks");
      formData.append("tasks", JSON.stringify(tasksArray));
      const request = sendRequest(requestOptions);
      request
        .then((data) => {
          showToastNotification(`${data["msg"]}`, "success");
          submitBtn.disabled = false;
          submitBtn.classList.remove("disabled", "cur-progress", "is-disabled");
          setTimeout(() => {
            window.location.reload();
          }, 1000);
        })
        .catch((error) => {
          console.error(error);
          showToastNotification(`${JSON.stringify(error["user_error_msg"])}`, "danger");
          submitBtn.disabled = false;
          submitBtn.classList.remove("disabled", "cur-progress", "is-disabled");
        });
      // currentTarget.submit();
    });
  }
});
