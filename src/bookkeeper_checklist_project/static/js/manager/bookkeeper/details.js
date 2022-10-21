"use strict";

document.addEventListener("readystatechange", (ev) => {
  // The document is still loading.
  /* if (document.readyState === "loading") {

    } */

  // The document has finished loading and the document has been parsed but sub-resources such as scripts, images, stylesheets and frames are still loading.
  /* if (document.readyState === "interactive") {

    } */

  // check if the page fully loaded with all resources
  if (document.readyState === "complete") {
    $(() => {
      $("#edit-preferences").click(function () {
        $("#edit-preferences-modal").addClass("is-active");
      });
      $(".modal-card-head button.delete, .modal-save, .modal-cancel").click(function () {
        $("#edit-preferences-modal").removeClass("is-active");
      });
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
      buttons: ["copy", "csv", "pdf"],
    });
  }
});
