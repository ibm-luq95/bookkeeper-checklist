"use strict";
import {
  isDisabledCssClass,
  eyeSlashIconHTMLCode,
  eyeIconHTMLCode,
} from "../../utils/constants.js";
import { showToastNotification } from "../../utils/notifications.js";

document.addEventListener("DOMContentLoaded", (readyEvent) => {
  const clipboardJs = new ClipboardJS(".copyBtn");
  const companyServicesTable = document.querySelector("table#companyServicesTable");
  const managerCSShowPasswordBtns = document.querySelectorAll("button.managerCSShowPasswordBtn");
  const managerCSCopyPasswordBtns = document.querySelectorAll("button.managerCSCopyPasswordBtn");
  const managerCSCopyEmailBtns = document.querySelectorAll("button.managerCSCopyEmailBtn");

  // copy email buttons
  if (managerCSCopyEmailBtns) {
    managerCSCopyEmailBtns.forEach((btn) => {
      btn.addEventListener("click", (event) => {
        const currentTarget = event.currentTarget;
        const email = currentTarget.dataset["emailValue"];
        navigator.clipboard.writeText(email);
        showToastNotification("Email/Username Copied successfully!", "success");
      });
    });
  }
  // copy password buttons
  if (managerCSCopyPasswordBtns) {
    managerCSCopyPasswordBtns.forEach((btn) => {
      btn.addEventListener("click", (event) => {
        const currentTarget = event.currentTarget;
        const inputId = currentTarget.dataset["inputId"];
        const passwordInput = companyServicesTable.querySelector(`input#${inputId}`);
        navigator.clipboard.writeText(passwordInput.value);
        showToastNotification("Password copied successfully!", "success");
      });
    });
  }
  // show password buttons
  if (managerCSShowPasswordBtns) {
    managerCSShowPasswordBtns.forEach((btn) => {
      btn.addEventListener("click", (event) => {
        const currentTarget = event.currentTarget;
        const isVisible = Boolean(parseInt(currentTarget.dataset["isVisible"]));
        const inputId = currentTarget.dataset["inputId"];
        const passwordInput = companyServicesTable.querySelector(`input#${inputId}`);
        if (isVisible === true) {
          currentTarget.innerHTML = eyeIconHTMLCode;
          currentTarget.dataset["isVisible"] = 0;
          passwordInput.type = "password";
        } else {
          currentTarget.innerHTML = eyeSlashIconHTMLCode;
          currentTarget.dataset["isVisible"] = 1;
          passwordInput.type = "text";
        }
      });
    });
  }
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

  const clientsTable = $("#companyServicesTable").DataTable({
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
    columnDefs: [{ orderable: false, targets: 7 }],
    order: [[6, "desc"]],
    // ordering: false,
    buttons: [
      // "copy",
      "csv",
      "pdf",
    ],
  });
});
