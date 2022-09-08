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
    allBkChLstInputs.forEach((element) => {
      element.disabled = false;
      element.classList.remove(isDisabledCssClass);
    });
    // Then instantiate the MicroModal module, so that it takes care of all the bindings for you.
    MicroModal.init({
      disableScroll: false,
    });

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
      if (textType === "username") {
        showToastNotification(`Username ${copiedText} copied successfully`, "success");
      } else if (textType === "password") {
        showToastNotification(`Password copied successfully`, "success");
      }
    });

    const acsSearchBtn = document.querySelector("#acsSearchBtn");
    acsSearchBtn.addEventListener("click", (event) => {
      const currentTarget = event.currentTarget;
      const searchAccountLoader = document.querySelector("#searchAccountLoader");
      const acServicesSearchInput = document.querySelector("#acServicesSearch");
      searchAccountLoader.hidden = false;
      currentTarget.disabled = true;
      acServicesSearchInput.disabled = true;
    });
  }
});
