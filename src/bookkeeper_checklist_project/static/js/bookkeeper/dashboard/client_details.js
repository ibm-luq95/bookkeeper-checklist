"use strict";
import {
  isDisabledCssClass,
  eyeSlashIconHTMLCode,
  eyeIconHTMLCode,
} from "../../utils/constants.js";
import { showToastNotification } from "../../utils/notifications.js";

document.addEventListener("readystatechange", (ev) => {
  // The document is still loading.
  if (document.readyState === "loading") {
  }

  // The document has finished loading and the document has been parsed but sub-resources such as scripts, images, stylesheets and frames are still loading.
  if (document.readyState === "interactive") {
  }

  // check if the page fully loaded with all resources
  if (document.readyState === "complete") {
    const clipboardJs = new ClipboardJS(".copyBtn");

    // first enable all bkchlst inputs when page fully loaded completed
    const allBkChLstInputs = document.querySelectorAll(".bkchlst-input");
    const inputTrimWhitespaceBtns = document.querySelectorAll(".input-trim-whitespace");
    allBkChLstInputs.forEach((element) => {
      const isDisabled = element.dataset["isDisabled"];
      if (isDisabled !== "1") {
        element.disabled = false;
        element.classList.remove(isDisabledCssClass);
      }
    });
    inputTrimWhitespaceBtns.forEach((element) => {
      element.value = element.value.trim();
    });
    // Then instantiate the MicroModal module, so that it takes care of all the bindings for you.
    MicroModal.init({
      disableScroll: false,
    });

    const weeklyTasksInputs = document.querySelectorAll(".monthly-task-checkbox");
    const weeklyTasksSubmitBtn = document.querySelector("#weeklyTasksSubmitBtn");

    // bookkeeper add new task button
    const bookkeeperAddNewTaskBtn = document.querySelector("#bookkeeperAddNewTaskBtn");
    bookkeeperAddNewTaskBtn.addEventListener("click", (event) => {
      MicroModal.show("add-new-task-modal", {
        disableScroll: false,
        onClose: (modal) => {
          console.info(`${modal.id} is hidden`);
        },
        disableFocus: false,
      });
    });

    // task items buttons
    const openTasksItemsModalBtns = document.querySelectorAll(".open-tasks-items-modal-btn");
    openTasksItemsModalBtns.forEach((element) => {
      element.addEventListener("click", (event) => {
        const currentTarget = event.currentTarget;
        MicroModal.show("tasks-items-modal", {
          disableScroll: false,
          onClose: (modal) => {
            console.info(`${modal.id} is hidden`);
          },
          disableFocus: false,
        });
      });
    });

    // delete task buttons
    const deleteTaskBtns = document.querySelectorAll(".delete-task-btn");
    deleteTaskBtns.forEach((btn) => {
      btn.addEventListener("click", (event) => {
        const currentTarget = event.currentTarget;
        alert("do you want to delete?");
      });
    });

    // tasks checkbox main checkbox event
    const tasksThMainCheckboxs = document.querySelectorAll(".tasks-th-main-checkbox");

    tasksThMainCheckboxs.forEach((element) => {
      element.addEventListener("change", (event) => {
        const currentTarget = event.currentTarget;

        const childeElementsCssClass = `.${currentTarget.dataset["childCheckboxClass"]}`;
        const allChildElements = document.querySelectorAll(childeElementsCssClass);
        allChildElements.forEach((input) => {
          console.log(weeklyTasksInputs);
          if (currentTarget.checked === true) {
            input.checked = true;
          } else {
            input.checked = false;
          }
        });
      });
    });

    document.querySelectorAll(".tablinks").forEach((element) => {
      element.addEventListener("click", (event) => {
        let i, tabcontent, tablinks;
        const clickedBtn = event.currentTarget;
        const data = clickedBtn.dataset;
        const tabContentId = data["tabElement"];
        tabcontent = document.querySelectorAll(".tabcontent");
        tabcontent.forEach((tabElement) => {
          tabElement.style.display = "none";
        });
        tablinks = document.querySelectorAll(".tablinks");
        tablinks.forEach((linkElement) => {
          linkElement.className = linkElement.className.replace("active", "");
        });
        document.querySelector(`#${tabContentId}`).style.display = "block";
        clickedBtn.classList.add("active");
      });
    });

    document.querySelectorAll(".tablinks2").forEach((element) => {
      element.addEventListener("click", (event) => {
        let i, tabcontent, tablinks;
        const clickedBtn = event.currentTarget;
        const data = clickedBtn.dataset;
        const tabContentId = data["tabElement"];
        tabcontent = document.querySelectorAll(".tabcontent2");
        tabcontent.forEach((tabElement) => {
          tabElement.style.display = "none";
        });
        tablinks = document.querySelectorAll(".tablinks2");
        tablinks.forEach((linkElement) => {
          linkElement.className = linkElement.className.replace("active", "");
        });
        document.querySelector(`#${tabContentId}`).style.display = "block";
        clickedBtn.classList.add("active");
      });
    });

    // Get the element with id="defaultOpen" and click on it
    // document.getElementById("defaultOpen").click();
    document.querySelectorAll(".defaultOpenTab1").forEach((element) => {
      element.click();
    });

    const acc = document.querySelectorAll(".accordion");
    let i;
    for (i = 0; i < acc.length; i++) {
      acc[i].addEventListener("click", function () {
        this.classList.toggle("active");
        let panel = this.nextElementSibling;
        if (panel.style.maxHeight) {
          panel.style.maxHeight = null;
        } else {
          panel.style.maxHeight = panel.scrollHeight + "px";
        }
      });
    }

    const copyASurlBtns = document.querySelectorAll(".copyASurlBtn");
    copyASurlBtns.forEach((btn) => {
      btn.addEventListener("click", (event) => {
        const currentTarget = event.currentTarget;
        const UrlInputId = currentTarget.dataset["clipboardTarget"];
        const UrlInputElement = document.querySelector(`${UrlInputId}`);
      });
    });

    const allShowASPasswordBtns = document.querySelectorAll(".showASUPasswordBtn");
    allShowASPasswordBtns.forEach((btn) => {
      btn.addEventListener("click", (event) => {
        const currentTarget = event.currentTarget;
        const visibilityStatus = Boolean(parseInt(currentTarget.dataset["visibilityStatus"]));
        const passwordInputId = currentTarget.dataset["passwordInput"];
        const passwordInputElement = document.querySelector(`#${passwordInputId}`);
        if (visibilityStatus === true) {
          currentTarget.innerHTML = eyeIconHTMLCode;
          currentTarget.dataset["visibilityStatus"] = 0;
          passwordInputElement.type = "password";
        } else {
          currentTarget.innerHTML = eyeSlashIconHTMLCode;
          currentTarget.dataset["visibilityStatus"] = 1;
          passwordInputElement.type = "text";
        }
      });
    });

    clipboardJs.on("success", (e) => {
      // console.info("Action:", e.action);
      // console.info("Text:", e.text);
      // console.info("Trigger:", e.trigger);
      e.clearSelection();
      const copiedText = e.text;
      const element = e.trigger;
      const textType = element.dataset["textType"];
      switch (textType) {
        case "username":
          showToastNotification(`Username ${copiedText} copied successfully`, "success");
          break;

        case "password":
          showToastNotification(`Password copied successfully`, "success");
          break;
        case "url":
          showToastNotification(`Url copied successfully`, "success");
          break;
      }
    });

    // open note item
    const allNotesItemsBtns = document.querySelectorAll(".open-note-item-btn");
    allNotesItemsBtns.forEach((element) => {
      element.addEventListener("click", (event) => {
        MicroModal.show("notes-item-modal", {
          disableScroll: false,
          onClose: (modal) => {
            console.info(`${modal.id} is hidden`);
          },
          disableFocus: false,
        });
      });
    });

    const tableFooterSearchElements = document.querySelectorAll(
      "#clientsAccountAndServicesTable tfoot th",
    );
    tableFooterSearchElements.forEach((element) => {
      const title = element.textContent;
      let inputID;
      switch (element.id) {
        case "footerUrl":
          inputID = "searchFooterUrl";
          break;
        case "footerUsername":
          inputID = "searchFooterUsername";
          break;
        case "footerPassword":
          inputID = "searchFooterPassword";
          break;
      }
      // element.innerHTML = '<input type="text" placeholder="Search ' + title + '" />';
      const searchInputElement = document.createElement("input");
      searchInputElement.type = "text";
      searchInputElement.id = inputID;
      searchInputElement.classList.add(...["input", "is-small", "searchTableFooterInput"]);
      searchInputElement.placeholder = `Search ${title}`;
      element.appendChild(searchInputElement);
    });

    const clientsAccountAndServicesTable = $("#clientsAccountAndServicesTable").DataTable({
      autoWidth: true,
      // processing: true,
      info: true,
      // "paging": false,
      // stateSave: true,
      stateSaveCallback: function (settings, data) {
        localStorage.setItem("DataTables_" + settings.sInstance, JSON.stringify(data));
      },
      stateLoadCallback: function (settings) {
        return JSON.parse(localStorage.getItem("DataTables_" + settings.sInstance));
      },
      fixedHeader: true,
      // responsive: true,
      columnDefs: [{ type: "html-input", targets: [0, 1, 2] }],
      // dom: "Bfrtip",
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
      // buttons: ["copy", "csv", "pdf"],
      initComplete: function () {
        // Apply the search
        this.api()
          .columns()
          .every(function () {
            let that = this;
            // console.log(this.footer());
            $("input", this.footer()).on("keyup change clear", function () {
              if (that.search() !== this.value) {
                that.search(this.value).draw();
              }
            });
          });
      },
    });
    // Apply the search
    clientsAccountAndServicesTable.columns().every(function () {
      let that = this;

      $("input", this.footer()).on("keyup change", function () {
        that.search(this.value).draw();
      });
    });
  }
});
