"use strict";

import {
  eyeIconHTMLCode,
  eyeSlashIconHTMLCode,
} from "../../utils/constants.js";
import { addTxtToClipboardWithNotification } from "../../utils/helpers.js";

document.addEventListener("DOMContentLoaded", (readyEvent) => {
  const copyInputBtns = document.querySelectorAll("button.copyInputBtn");
  const showInputPasswordBtns = document.querySelectorAll(
    "button.showInputPasswordBtn"
  );

  // all copy buttons event handler
  if (copyInputBtns) {
    copyInputBtns.forEach((input) => {
      input.addEventListener("click", (event) => {
        const currentTarget = event.currentTarget;
        const copiedValue = currentTarget.dataset["copiedValue"];
        const textType = currentTarget.dataset["textType"];
        addTxtToClipboardWithNotification({
          textWillCopy: copiedValue,
          label: textType,
        });
      });
    });
  }

  // show password buttons event handler
  if (showInputPasswordBtns) {
    showInputPasswordBtns.forEach((input) => {
      input.addEventListener("click", (event) => {
        const currentTarget = event.currentTarget;
        const isVisible = Boolean(parseInt(currentTarget.dataset["isVisible"]));
        const inputId = currentTarget.dataset["inputId"];
        const passwordInput = document.querySelector(`input#${inputId}`);
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
