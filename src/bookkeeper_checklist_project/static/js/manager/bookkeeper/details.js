"use strict";

import { getCookie } from "../../utils/cookie.js";
import { enableInputsOnLoad, sendRequest } from "../../utils/helpers.js";
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

    let tabsWithContent = (function () {
      let tabs = document.querySelectorAll(".tabs li");
      let tabsContent = document.querySelectorAll(".tab-content");

      let deactvateAllTabs = function () {
        tabs.forEach(function (tab) {
          tab.classList.remove("is-active");
        });
      };

      let hideTabsContent = function () {
        tabsContent.forEach(function (tabContent) {
          tabContent.classList.remove("is-active");
        });
      };

      let activateTabsContent = function (tab) {
        tabsContent[getIndex(tab)].classList.add("is-active");
      };

      let getIndex = function (el) {
        return [...el.parentElement.children].indexOf(el);
      };

      tabs.forEach(function (tab) {
        tab.addEventListener("click", function () {
          deactvateAllTabs();
          hideTabsContent();
          tab.classList.add("is-active");
          activateTabsContent(tab);
        });
      });

      tabs[0].click();
    })();

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
      /* buttons: [
      {
        extend: "alert",
        text: "My button 1",
      },
      {
        extend: "alert",
        text: "My button 2",
      },
      {
        extend: "alert",
        text: "My button 3",
      },
    ], */
      buttons: [
        "copy",
        "csv",
        "pdf",
        {
          text: "Add New Job",
          className: "is-success",
          action: (e, dt, node, config) => {
            // console.log(config);
            // alert("Button activated");
            // dt.data.reload();
            MicroModal.show("jobs-form-modal", {
              disableScroll: false,
              onClose: (modal) => {
                console.info(`${modal.id} is hidden`);
              },
              disableFocus: false,
            });
          },
        },
      ],
    });

    const managerAddNewJobForm = document.querySelector("#managerAddNewJobForm");
    managerAddNewJobForm.addEventListener("submit", (event) => {
      event.preventDefault();
      const currentTarget = event.currentTarget;
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
          setTimeout(() => {
            window.location.reload();
          }, 1500);
        })
        .catch((error) => {
          console.error(error);
          showToastNotification(`${JSON.stringify(error["user_error_msg"])}`, "danger");
        });
      // currentTarget.submit();
    });
  }
});
