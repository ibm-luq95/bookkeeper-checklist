"use strict";

document.addEventListener("DOMContentLoaded", (readyEvent) => {
  const templateCode = `
      <div id="jobTemplateModal" class="tingle-modal has-ribbon">
        <div class="ribbon is-primary">Status</div>
        <h4 class="title is-4 mt-1" id="jobTemplateTitle">Job template title</h4>
        <hr />
        <div class="content">
            <p class="has-text-justified mb-4" id="jobTemplateDescription">
                Lorem ipsum leo risus, porta ac consectetur ac, vestibulum at eros. Donec id elit non mi porta gravida at
                eget
                metus. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Cras mattis
                consectetur purus sit amet fermentum.
            </p>
            <div id="jobTemplateStatus" class="mb-4">
                <strong>Status:</strong> <span class="tag is-medium">Active</span>
            </div>
            <div id="jobTemplateType" class="mb-4">
                <strong>Type:</strong> <span class="tag is-medium">Type</span>
            </div>
            <div id="jobTemplateTasks" class="mb-4">
                <h6 class="job-template-label">Tasks</h6>
                <ol>
                    <li>Task 1</li>
                    <li>Task 2</li>
                    <li>Task 3</li>
                    <li>Task 4</li>
                </ol>
            </div>
            <div id="jobTemplateDocuments" class="mb-4">
                <h6 class="job-template-label">Documents</h6>
                <ol>
                    <li>Documents 1</li>
                    <li>Documents 2</li>
                    <li>Documents 3</li>
                    <li>Documents 4</li>
                </ol>
            </div>
            <div id="jobTemplateNotes" class="mb-4">
                <h6 class="job-template-label">Notes</h6>
                <ol>
                    <li>Notes 1</li>
                    <li>Notes 2</li>
                    <li>Notes 3</li>
                    <li>Notes 4</li>
                </ol>
            </div>
            <div id="jobTemplateCategories" class="mb-4">
                <h6 class="job-template-label">Categories</h6>
                <div class="tags are-small">
                    <a class="tag is-primary is-light">One</a>
                    <a class="tag is-primary is-light">Two</a>
                    <a class="tag is-primary is-light">Three</a>
                </div>
            </div>
            <div id="jobTemplateCreatedAt" class="mt-5">
                <strong>
                    <time class="hint--top" aria-label="Created at" datetime="2008-02-14 20:00">2008-02-14 20:00</time>
                </strong>
            </div>
        </div>
    </div>
  `;
  const template = document.createElement("template");
  template.innerHTML = templateCode;

  // define the web content
  class JobTemplateModal extends HTMLElement {
    constructor() {
      super();
      this.attachShadow({ mode: "open" });
      this.shadowRoot.appendChild(template.content.cloneNode(true));
    }
  }

  window.customElements.define("job-template-modal", JobTemplateModal);
});
