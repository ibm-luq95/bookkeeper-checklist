"use strict";
import {
    checkIfInputSingleOrList,
    fetchUrlPathByName,
    formInputSerializer,
    sendRequest,
  } from "../../utils/helpers.js";
  import { MicroModalHandler } from "../../utils/model-box.js";
  import { showToastNotification } from "../../utils/notifications.js";

  document.addEventListener("DOMContentLoaded", (readyEvent) => {
    const jobFormModalId = "job-form-modal";
    const jobFormModalElement = document.querySelector(`#${jobFormModalId}`);
    const jobModalTitleElement =
      jobFormModalElement.querySelector(".modal__title");
    const jobModalSubmitBtn = jobFormModalElement.querySelector(
      "button[type='submit']"
    );
    // const jobsFormWrapper = document.querySelector("div#jobsFormWrapper");
    const managerJobsLoaderBtn = document.querySelector(
      "button#managerJobsLoaderBtn"
    );
    // const jobsForm = jobsFormWrapper.querySelector("form#jobsForm");
    const jobsForm = jobFormModalElement.querySelector("form");
    const jobsFormFieldset = jobsForm.querySelector("fieldset");
    const addJobBtn = document.querySelector("button#addJobBtn");
    const managerDeleteJobBtn = document.querySelectorAll(
      "button.managerDeleteJobBtn"
    );

    const managerViewJobBtn = document.querySelectorAll(
      "button.managerViewJobBtn"
    );

    addJobBtn.addEventListener("click", (event) => {
      const callBacks = {
        onOpenCallBack: async () => {
          const createJobUrl = await fetchUrlPathByName(
            "jobs:api:create"
          );
          jobModalSubmitBtn.textContent = "Create";
          jobsForm.elements["_method"].value = "POST";
          jobsForm.setAttribute("method", "POST");
          jobsForm.setAttribute("action", createJobUrl["urlPath"]);
          jobModalTitleElement.textContent = "Create new job";
        },
        onCloseCallback: () => {
          jobModalSubmitBtn.disabled = false;
          // jobsForm.reset();
        },
      };
      const modalHandler = new MicroModalHandler(jobFormModalId, callBacks);
    });

    // create new job form event
    jobsForm.addEventListener("submit", async (event) => {
      event.preventDefault();
      try {
        const updateJobUrl = await fetchUrlPathByName("jobs:api:update");
        const currentTarget = event.currentTarget;
        jobsFormFieldset.disabled = true;
        managerJobsLoaderBtn.hidden = false;
        const bookkeepersArray = new Array();
        const assistantsArray = new Array();
        const tasksArray = new Array();
        Array.from(jobsForm.elements).forEach((element) => {
          element.classList.remove("is-danger");
        });

        // check if bookkeeper exists
        if (jobsForm["bookkeeper"]) {
          // check if bookkeeper single or multiple
          if (checkIfInputSingleOrList(jobsForm["bookkeeper"]) === "multiple") {
            jobsForm["bookkeeper"].forEach((input) => {
              if (input.checked === true) {
                bookkeepersArray.push(input.value);
              }
            });
          } else {
            if (jobsForm["bookkeeper"].checked === true) {
              bookkeepersArray.push(jobsForm["bookkeeper"].value);
            }
          }
        }
        // check if assistants exists
        if (jobsForm["assistants"]) {
          // check if assistants single or multiple
          if (checkIfInputSingleOrList(jobsForm["assistants"]) === "multiple") {
            jobsForm["assistants"].forEach((input) => {
              if (input.checked === true) {
                assistantsArray.push(input.value);
              }
            });
          } else {
            if (jobsForm["assistants"].checked === true) {
              assistantsArray.push(jobsForm["assistants"].value);
            }
          }
        }
        // check if tasks exists
        if (jobsForm["tasks"]) {
          // check if tasks one element or multiple
          if (checkIfInputSingleOrList(jobsForm["tasks"]) === "multiple") {
            // in case multiple tasks
            jobsForm["tasks"].forEach((input) => {
              if (input.checked === true) {
                tasksArray.push(input.value);
              }
            });
          } else {
            if (jobsForm["tasks"].checked === true) {
              tasksArray.push(jobsForm["tasks"].value);
            }
          }
        }

        // throw new Error("s");
        const formInputs = formInputSerializer({
          formElement: jobsForm,
          excludedFields: ["bookkeeper", "tasks", "_method", "assistants"],
          isOrdered: true,
        });
        formInputs["tasks"] = tasksArray;
        formInputs["bookkeeper"] = bookkeepersArray;
        formInputs["assistants"] = assistantsArray;
        if (jobsForm["_method"].value === "PUT") {
          formInputs["jobId"] = jobsForm["jobId"].value;
        }
        // console.log(formInputs);
        // throw new Error("Stop");
        const requestOptions = {
          method: jobsForm["_method"].value,
          dataToSend: formInputs,
          url: jobsForm.action,
        };
        const request = sendRequest(requestOptions);
        request
          .then((data) => {
            console.log(data);
            showToastNotification(data["msg"], "success");
            setTimeout(() => {
              window.location.reload();
            }, 500);
          })
          .catch((error) => {
            console.error(error);
            showToastNotification(
              `${JSON.stringify(error["user_error_msg"])}`,
              "danger"
            );
            const userErrors = error["user_error_msg"];
            for (const key in userErrors) {
              if (Object.hasOwnProperty.call(userErrors, key)) {
                const element = userErrors[key];
                jobsForm[key].classList.add(...["is-danger"]);
              }
            }
          })
          .finally(() => {
            jobsFormFieldset.disabled = false;
            managerJobsLoaderBtn.hidden = true;
          });
      } catch (error) {
        console.error(error);
        jobsFormFieldset.disabled = false;
        managerJobsLoaderBtn.hidden = true;
      }
    });

    // delete job buttons
    managerDeleteJobBtn.forEach((btn) => {
      // @audit
      btn.addEventListener("click", async (event) => {
        // const deleteJobUrl = window.localStorage.getItem("DeleteJobUrl");

        const jobId = event.currentTarget.dataset["jobId"];
        const jobTitle = event.currentTarget.dataset["jobTitle"];
        const deleteJobUrl = await fetchUrlPathByName("jobs:api:delete");
        const requestOptions = {
          method: "DELETE",
          dataToSend: { jobId: jobId },
          url: deleteJobUrl["urlPath"],
        };
        const msg = confirm(`Do you want to delete ${jobTitle}?`);
        if (msg) {
          const request = sendRequest(requestOptions);
          request
            .then((data) => {
              // console.log(data);
              // check if job contains any tasks
              if (data["is_allowed_deleted"] === false) {
                showToastNotification(data["msg"], "info");
              } else {
                showToastNotification(data["msg"], "success");
                setTimeout(() => {
                  window.location.reload();
                }, 500);
              }
            })
            .catch((error) => {
              console.error(error);
              showToastNotification(
                `${JSON.stringify(error["user_error_msg"])}`,
                "danger"
              );
            });
        }
      });
    });

    // view job buttons
    managerViewJobBtn.forEach((btn) => {
      btn.addEventListener("click", async (event) => {
        const jobsUpdateFormFieldSet = jobsForm.querySelector("fieldset");
        const jobId = event.currentTarget.dataset["jobId"];
        // const url = window.localStorage.getItem("RetrieveJobUrl");
        const retrieveUrl = await fetchUrlPathByName("jobs:api:retrieve");
        const updateJobUrl = await fetchUrlPathByName("jobs:api:update");

        // job-details-update-modal @audit
        const callBacks = {
          onOpenCallBack: () => {
            // console.log("Open update job");
            jobModalTitleElement.textContent = "Update job";
            jobModalSubmitBtn.textContent = "Update";
            jobsForm.setAttribute("action", updateJobUrl["urlPath"]);
            jobsForm.setAttribute("method", "PUT");
            jobsForm["_method"].value = "PUT";
            const requestOptions = {
              method: "POST",
              dataToSend: { jobId: jobId },
              url: retrieveUrl["urlPath"],
            };
            const request = sendRequest(requestOptions);
            request
              .then((data) => {
                // console.log(data);
                const jobObject = data["job"];
                const bookkeepers = jobObject["bookkeeper"];
                const bookkeepersIds = bookkeepers.map(
                  (element) => element["id"]
                );
                const tasks = jobObject["tasks"];
                // console.log(jobObject);
                jobsForm["title"].value = jobObject["title"];
                jobsForm["description"].value = jobObject["description"];
                jobsForm["due_date"].value = jobObject["due_date"];
                jobsForm["job_type"].value = jobObject["job_type"];
                jobsForm["status"].value = jobObject["status"];
                // jobsForm["client"].value = jobObject["client"];
                jobsForm["note"].value = jobObject["note"];
                jobsForm["jobId"].value = jobObject["id"];

                // RadioNodeList: multiple radio inputs,
                // HTMLInputElement: one radio input
                // console.log(jobsForm["jobId"].value);
                // check the bookkeeper array length
                if (bookkeepersIds.length > 0) {
                  // check if the bookkeeper one or more than one input
                  if (
                    jobsForm["bookkeeper"].constructor.name === "HTMLInputElement"
                  ) {
                    // one input
                    const filtered = bookkeepersIds.some(
                      (ele) => ele == jobsForm["bookkeeper"].value
                    );
                    if (filtered === true) {
                      jobsForm["bookkeeper"].checked = true;
                    }
                  } else if (
                    jobsForm["bookkeeper"].constructor.name === "RadioNodeList"
                  ) {
                    // two inputs
                    jobsForm["bookkeeper"].forEach((input) => {
                      const filtered = bookkeepersIds.some(
                        (ele) => ele == input.value
                      );
                      // check if filtered is true
                      if (filtered === true) {
                        input.checked = true;
                      }
                    });
                  }
                }

                // generate tasks checkbox elements
                if (tasks.length > 0) {
                  tasks.forEach((taskElement) => {
                    const fieldElement = document.createElement("div");
                    fieldElement.classList.add(
                      ...["field", "jobUpdateTasksField"]
                    );
                    const label = document.createElement("label");
                    label.classList.add(...["checkbox", "is-block", "my-2"]);
                    const taskCheckbox = document.createElement("input");
                    taskCheckbox.type = "checkbox";
                    taskCheckbox.name = "tasks";
                    taskCheckbox.checked = true;
                    taskCheckbox.value = taskElement["id"];
                    taskCheckbox.classList.add(...["mr-1"]);
                    label.textContent = taskElement["title"];
                    label.prepend(taskCheckbox);
                    fieldElement.appendChild(label);
                    jobsUpdateFormFieldSet.appendChild(fieldElement);
                  });
                }
                // console.log(tasks);

                /* Array.from(jobsUpdateForm.elements).forEach((element) => {
                    console.log(element);
                  }); */
                // showToastNotification(data["msg"], "success");
                /* setTimeout(() => {
                    window.location.reload();
                  }, 500); */
              })
              .catch((error) => {
                console.error(error);
                showToastNotification(
                  `${JSON.stringify(error["user_error_msg"])}`,
                  "danger"
                );
              })
              .finally(() => {
                jobsFormFieldset.disabled = false;
                managerJobsLoaderBtn.hidden = true;
              });
          },
          onCloseCallback: () => {
            console.warn("Close Update job");
            const allTasksFields = document.querySelectorAll(
              "div.jobUpdateTasksField"
            );
            allTasksFields.forEach((element) => {
              element.remove();
            });
            jobsForm.reset();
          },
        };
        new MicroModalHandler(jobFormModalId, callBacks);
        /* jobsUpdateForm.addEventListener("submit", (event) => {
            event.preventDefault();
            const currentTarget = event.currentTarget;
            const updateUrl = currentTarget.action;
            const checkedTasks = new Array();
            const checkedBookkeepers = new Array();

            // check if the bookkeeper one or more than one input
            if (
              currentTarget["bookkeeper"].constructor.name === "HTMLInputElement"
            ) {
              // one input
              if (currentTarget["bookkeeper"].checked === true) {
                checkedBookkeepers.push(currentTarget["bookkeeper"].value);
              }
            } else if (
              currentTarget["bookkeeper"].constructor.name === "RadioNodeList"
            ) {
              // two inputs
              currentTarget["bookkeeper"].forEach((input) => {
                if (input.checked === true) {
                  checkedBookkeepers.push(input.value);
                }
              });
            }
            // check if tasks exists
            if (currentTarget["tasks"]) {
              // check if the tasks one or more than one input
              if (currentTarget["tasks"].constructor.name === "HTMLInputElement") {
                // one input
                if (currentTarget["tasks"].checked === true) {
                  checkedTasks.push(currentTarget["tasks"].value);
                }
              } else if (
                currentTarget["tasks"].constructor.name === "RadioNodeList"
              ) {
                // two inputs
                currentTarget["tasks"].forEach((e) => {
                  if (e.checked === true) {
                    checkedTasks.push(e.value);
                  }
                });
              }
            }

            // console.log("checkedTasks: ", checkedTasks);
            // console.log("checkedBookkeepers: ", checkedBookkeepers);
            const formData = {
              jobId: currentTarget["jobId"].value,
              bookkeeper: checkedBookkeepers,
              tasks: checkedTasks,
              client: currentTarget["client"].value,
              title: currentTarget["title"].value,
              description: currentTarget["description"].value,
              note: currentTarget["note"].value,
              job_type: currentTarget["job_type"].value,
              status: currentTarget["status"].value,
              due_date: currentTarget["due_date"].value,
            };
            console.log(formData);
            const requestOptions = {
              method: "PUT",
              dataToSend: formData,
              url: currentTarget.action,
            };
            const request = sendRequest(requestOptions);
            request
              .then((data) => {
                console.log(data);
                showToastNotification("Job updated successfully", "success");
                setTimeout(() => {
                  window.location.reload();
                }, 500);
              })
              .catch((error) => {
                console.error(error);
                showToastNotification(
                  `${JSON.stringify(error["user_error_msg"])}`,
                  "danger"
                );
              });
          }); */
      });
    });
  });
