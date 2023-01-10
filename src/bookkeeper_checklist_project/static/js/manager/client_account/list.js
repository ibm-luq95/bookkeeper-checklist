"use strict";

import {
  eyeIconHTMLCode,
  eyeSlashIconHTMLCode,
} from "../../utils/constants.js";
import { DataTableHelper } from "../../utils/datatable-helper.js";
import { showToastNotification } from "../../utils/notifications.js";

document.addEventListener("DOMContentLoaded", (ev) => {
  /*
    the browser fully loaded HTML, and the DOM tree is built, but external resources like pictures <img> and stylesheets may not yet have loaded.
    */
  const managerClientAccountTable = document.querySelector(
    "table#managerClientAccountTable"
  );
  const managerCAShowPasswordBtns = document.querySelectorAll(
    "button.managerCAShowPasswordBtn"
  );

  const managerCACopyPasswordBtns = document.querySelectorAll(
    "button.managerCACopyPasswordBtn"
  );
  const managerCACopyEmailBtns = document.querySelectorAll(
    "button.managerCACopyEmailBtn"
  );
  const managerCACopyURLBtns = document.querySelectorAll(
    "button.managerCACopyURLBtn"
  );
  const managerCACopyUsernameBtns = document.querySelectorAll(
    "button.managerCACopyUsernameBtn"
  );
  new DataTableHelper({
    tableID: "managerClientAccountTable",
  });

  // copy email buttons
  if (managerCACopyEmailBtns) {
    managerCACopyEmailBtns.forEach((btn) => {
      btn.addEventListener("click", (event) => {
        const currentTarget = event.currentTarget;
        const email = currentTarget.dataset["emailValue"];
        navigator.clipboard.writeText(email);
        showToastNotification("Email copied successfully!", "success");
      });
    });
  }
  // copy username buttons
  if (managerCACopyUsernameBtns) {
    managerCACopyUsernameBtns.forEach((btn) => {
      btn.addEventListener("click", (event) => {
        const currentTarget = event.currentTarget;
        const username = currentTarget.dataset["usernameValue"];
        navigator.clipboard.writeText(username);
        showToastNotification("Username copied successfully!", "success");
      });
    });
  }
  // copy urls buttons
  if (managerCACopyURLBtns) {
    managerCACopyURLBtns.forEach((btn) => {
      btn.addEventListener("click", (event) => {
        const currentTarget = event.currentTarget;
        const url = currentTarget.dataset["urlValue"];
        navigator.clipboard.writeText(url);
        showToastNotification("URL copied successfully!", "success");
      });
    });
  }

  // copy password buttons
  if (managerCACopyPasswordBtns) {
    managerCACopyPasswordBtns.forEach((btn) => {
      btn.addEventListener("click", (event) => {
        const currentTarget = event.currentTarget;
        const inputId = currentTarget.dataset["inputId"];
        const passwordInput = managerClientAccountTable.querySelector(
          `input#${inputId}`
        );
        navigator.clipboard.writeText(passwordInput.value);
        showToastNotification("Password copied successfully!", "success");
      });
    });
  }

  // show password buttons
  if (managerCAShowPasswordBtns) {
    managerCAShowPasswordBtns.forEach((btn) => {
      btn.addEventListener("click", (event) => {
        const currentTarget = event.currentTarget;
        const isVisible = Boolean(parseInt(currentTarget.dataset["isVisible"]));
        const inputId = currentTarget.dataset["inputId"];
        const passwordInput = managerClientAccountTable.querySelector(
          `input#${inputId}`
        );
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
});
