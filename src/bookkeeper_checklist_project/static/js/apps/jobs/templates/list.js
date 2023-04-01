"use strict";

import { fadeIn, fadeOut, fetchUrlPathByName, sendGetRequest } from "../../../utils/helpers.js";
import { MicroModalHandler, TingleModalHandler } from "../../../utils/model-box.js";

document.addEventListener("DOMContentLoaded", (readyEvent) => {
  const jobModalId = "job-template-details";
  const jobModalElement = document.querySelector(`div#${jobModalId}`);

  const jobTemplatePreviewBtns = document.querySelectorAll("button.job-template-preview-btn");
  if (jobTemplatePreviewBtns) {
    jobTemplatePreviewBtns.forEach((btn) => {
      btn.addEventListener("click", async (event) => {
        const currentTarget = event.currentTarget;
        const jobId = currentTarget.dataset["jobId"];
        const loaderId = ".job-abstract-loader-component";

        // Edit link element
        const jobTemplateEditLink = jobModalElement.querySelector("a#jobTemplateEditLink");

        // Ribbon element
        const jobTemplateStatusRibbonElement = jobModalElement.querySelector(
          "div#jobTemplateStatusRibbon",
        );
        const jobTemplateStatusRibbonLoaderElement = jobModalElement.querySelector(loaderId);

        // Title element
        const jobTemplateTitleElement = jobModalElement.querySelector("#jobTemplateTitle");
        const jobTemplateTitleElementLoaderElement = jobModalElement.querySelector(loaderId);

        // Description element
        const jobTemplateDescriptionWrapperEle = jobModalElement.querySelector(
          "#jobTemplateDescriptionWrapper",
        );
        const jobTemplateDescriptionElement =
          jobTemplateDescriptionWrapperEle.querySelector("#jobTemplateDescription");
        const jobTemplateDescriptionLoaderElement =
          jobTemplateDescriptionWrapperEle.querySelector(loaderId);

        // Status element
        const jobTemplateStatusWrapperEle = jobModalElement.querySelector(
          "#jobTemplateStatusWrapper",
        );
        const jobTemplateStatusElement =
          jobTemplateStatusWrapperEle.querySelector("#jobTemplateStatus");
        const jobTemplateStatusElementTagElement =
          jobTemplateStatusWrapperEle.querySelector(".content-wrapper");
        const jobTemplateStatusElementLoaderElement =
          jobTemplateStatusWrapperEle.querySelector(loaderId);

        // Type element
        const jobTemplateTypeWrapperEle = jobModalElement.querySelector("#jobTemplateTypeWrapper");
        const jobTemplateTypeElement = jobTemplateTypeWrapperEle.querySelector(".content-wrapper");
        const jobTemplateTypeElementLoaderElement =
          jobTemplateTypeWrapperEle.querySelector(loaderId);

        // Tasks element
        const jobTemplateTasksWrapperEle = jobModalElement.querySelector(
          "#jobTemplateTasksWrapper",
        );
        const jobTemplateTasksElement =
          jobTemplateTasksWrapperEle.querySelector(".content-wrapper");
        const jobTemplateTasksElementLoaderElement =
          jobTemplateTasksWrapperEle.querySelector(loaderId);
        const jobTemplateTasksNotificationElement =
          jobTemplateTasksWrapperEle.querySelector(".notification");

        // Documents element
        const jobTemplateDocumentsWrapperElement = jobModalElement.querySelector(
          "#jobTemplateDocumentsWrapper",
        );
        const jobTemplateDocumentsLoaderElement =
          jobTemplateDocumentsWrapperElement.querySelector(loaderId);
        const jobTemplateDocumentsNotificationElement =
          jobTemplateDocumentsWrapperElement.querySelector(".notification");
        const jobTemplateDocumentsElement =
          jobTemplateDocumentsWrapperElement.querySelector(".content-wrapper");

        // Notes element
        const jobTemplateNotesWrapperEle = jobModalElement.querySelector(
          "#jobTemplateNotesWrapper",
        );
        const jobTemplateNotesLoaderElement = jobTemplateNotesWrapperEle.querySelector(loaderId);
        const jobTemplateNotesNotificationElement =
          jobTemplateNotesWrapperEle.querySelector(".notification");
        const jobTemplateNotesElement =
          jobTemplateNotesWrapperEle.querySelector(".content-wrapper");

        // Categories element
        const jobTemplateCategoriesWrapperEle = jobModalElement.querySelector(
          "#jobTemplateCategoriesWrapper",
        );
        const jobTemplateCategoriesElement =
          jobTemplateCategoriesWrapperEle.querySelector(".content-wrapper");
        const jobTemplateCategoriesTagsElement =
          jobTemplateCategoriesElement.querySelector(".tags");
        const jobTemplateCategoriesLoaderElement =
          jobTemplateCategoriesWrapperEle.querySelector(loaderId);

        // Created at element
        const jobTemplateCreatedAtWrapperEle = jobModalElement.querySelector(
          "#jobTemplateCreatedAtWrapper",
        );
        const jobTemplateCreateAtLoaderElement =
          jobTemplateCreatedAtWrapperEle.querySelector(loaderId);
        const jobTemplateCreatedAtElement = jobTemplateCreatedAtWrapperEle.querySelector("time");

        const url = await fetchUrlPathByName("jobs:api:templates:retrieve", jobId);
        const detailsJobUrl = await fetchUrlPathByName("jobs:templates:details", jobId);
        // console.log(url);

        const callBacks = {
          onCloseCallback: () => {
            const allOlElements = jobModalElement.querySelectorAll("ol.olElement");
            allOlElements.forEach((element) => {
              element.remove();
            });
            jobTemplateTitleElement.textContent = "";
            jobTemplateDescriptionElement.textContent = "";
            jobTemplateStatusElementTagElement.hidden = true;
            jobTemplateStatusElementTagElement.textContent = "";
            jobTemplateTypeElement.hidden = true;
            jobTemplateTypeElement.textContent = "";
          },
          onOpenCallBack: () => {
            console.log("%c Opened", "color: green;");
            const requestOptions = {
              method: "GET",
              url: url["urlPath"],
            };
            const request = sendGetRequest(requestOptions);
            request
              .then((data) => {
                console.log(data);
                jobTemplateDescriptionLoaderElement.hidden = true;
                jobTemplateStatusElementLoaderElement.classList.add("hidden");
                jobTemplateTypeElementLoaderElement.classList.add("hidden");
                jobTemplateTasksElementLoaderElement.classList.add("hidden");
                jobTemplateDocumentsLoaderElement.classList.add("hidden");
                jobTemplateNotesLoaderElement.classList.add("hidden");
                jobTemplateCategoriesLoaderElement.classList.add("hidden");
                jobTemplateCreateAtLoaderElement.classList.add("hidden");

                jobTemplateStatusRibbonElement.textContent = data["status_display"];
                if (data["status"] === "draft") {
                  jobTemplateStatusRibbonElement.classList.remove("is-primary");
                  jobTemplateStatusRibbonElement.classList.add("is-warning");
                } else {
                  jobTemplateStatusRibbonElement.classList.add("is-primary");
                  jobTemplateStatusRibbonElement.classList.remove("is-warning");
                }
                jobTemplateTitleElement.textContent = data["title"];
                jobTemplateDescriptionElement.textContent = data["description"];
                jobTemplateStatusElementTagElement.hidden = false;
                jobTemplateStatusElementTagElement.textContent = data["status_display"];
                jobTemplateTypeElement.hidden = false;
                jobTemplateTypeElement.textContent = data["type_display"];
                // start tasks element
                jobTemplateTasksElement.hidden = false;
                if (data["tasks"].length > 0) {
                  jobTemplateTasksNotificationElement.hidden = true;
                  //jobTemplateTasksElement
                  const olElement = document.createElement("ol");
                  olElement.classList.add("olElement");
                  for (const taskEItem of data["tasks"]) {
                    const liElement = document.createElement("li");
                    liElement.textContent = taskEItem["title"];
                    liElement.classList.add("small-font-size");
                    olElement.appendChild(liElement);
                  }
                  jobTemplateTasksElement.appendChild(olElement);
                } else {
                  // jobTemplateTasksElement.hidden = false;
                  jobTemplateTasksNotificationElement.hidden = false;
                }

                // start documents element
                jobTemplateDocumentsElement.hidden = false;
                if (data["documents"].length > 0) {
                  jobTemplateDocumentsNotificationElement.hidden = true;
                  const olElement = document.createElement("ol");
                  olElement.classList.add("olElement");
                  for (const documentItem of data["documents"]) {
                    const liElement = document.createElement("li");
                    const aElement = document.createElement("a");
                    aElement.textContent = documentItem["title"];
                    aElement.classList.add("small-font-size");
                    aElement.href = documentItem["template_file"];
                    aElement.download = documentItem["template_file"];
                    liElement.appendChild(aElement);
                    olElement.appendChild(liElement);
                  }

                  jobTemplateDocumentsElement.appendChild(olElement);
                } else {
                  jobTemplateDocumentsNotificationElement.hidden = false;
                }

                // start notes element
                jobTemplateNotesElement.hidden = false;
                if (data["notes"].length > 0) {
                  jobTemplateNotesNotificationElement.hidden = true;
                  const olElement = document.createElement("ol");
                  olElement.classList.add("olElement");
                  for (const noteItem of data["notes"]) {
                    const liElement = document.createElement("li");
                    liElement.textContent = noteItem["title"];
                    olElement.appendChild(liElement);
                  }
                  jobTemplateNotesElement.appendChild(olElement);
                } else {
                  jobTemplateNotesNotificationElement.hidden = false;
                }

                // start categories
                jobTemplateCategoriesElement.hidden = false;
                if (data["categories"].length > 0) {
                  jobTemplateCategoriesLoaderElement.hidden = true;
                  const olElement = document.createElement("ol");
                  olElement.classList.add("olElement");
                  for (const category of data["categories"]) {
                    //jobTemplateCategoriesTagsElement
                    const catElement = document.createElement("span");
                    catElement.classList.add(...["tag", "is-primary", "is-light"]);
                    catElement.textContent = category["name"];
                    jobTemplateCategoriesTagsElement.appendChild(catElement);
                  }
                } else {
                  jobTemplateCategoriesLoaderElement.hidden = false;
                }

                // start create at element
                jobTemplateCreatedAtElement.textContent = data["created_at"];
                jobTemplateCreatedAtElement.dateTime = data["created_at"];
                
                // set the job details href
                jobTemplateEditLink.href = detailsJobUrl["urlPath"];
              })
              .catch((error) => {
                console.error(error);
              });
          },
        };
        // new TingleModalHandler(jobModalId, callBacks);
        // console.log(jobTemplateStatusRibbonElement.querySelector(loaderId));
        new MicroModalHandler(jobModalId, callBacks);
      });
    });
  }
});
