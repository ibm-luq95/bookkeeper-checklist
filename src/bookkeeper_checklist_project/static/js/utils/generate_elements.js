"use strict";

class GenerateTagElement {
  /**
   * Generate tag element and return it
   * @typedef param
   * @param {Object} param - this is object param
   * @param {string} param.tagText Tag text
   * @param {string} param.tagColor Tag color
   * @param {string} param.elementType Element type span or a
   * @param {string} param.elementSize Tag size
   */
  constructor({
    tagText,
    tagColor = null,
    elementType = "span",
    elementSize = "is-small",
    isLight = false,
  }) {
    this.elementType = elementType;
    this.elementSize = elementSize;
    this.tagText = tagText;
    this.tagColor = tagColor;
    if (isLight === true) {
      this.isLight = "is-light";
    }
  }

  getGeneratedElement() {
    const element = document.createElement(this.elementType);
    element.classList.add(...["tag", this.elementSize, this.tagColor, this.isLight, "bk-tag"]);
    element.textContent = this.tagText;
    return element;
  }
}

export { GenerateTagElement };
