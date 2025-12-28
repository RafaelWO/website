document.addEventListener("DOMContentLoaded", function () {

  // Get code blocks
  const codeblocks = document.querySelectorAll(".highlight");

  // Iterate over each to perform modifications
  codeblocks.forEach((codeblock) => {
    // Create copy button and container element
    const copyButton = document.createElement("button");
    copyButton.className = "copy-button";
    const wrapper = document.createElement("div");
    wrapper.className = "code-container";

    // Copy clicked closure
    copyButton.addEventListener("click", (e) => {
      e.target.className = "copy-success";
      setTimeout(() => {
        e.target.className = "copy-button";
      }, 1000);


      const code = codeblock.textContent

      // if code has inline line numbers, remove them
      if (code.match(/\s*1/)) {
        let lines = code.split("\n")
        let lineNoIndent = lines.length.toString().length
        for (var i = 0; i < lines.length; i++) {
          lines[i] = lines[i].slice(lineNoIndent)
        }
        navigator.clipboard.writeText(lines.join("\n"));
      }
      else {
        navigator.clipboard.writeText(code);
      }
    });

    // Add the copy button to the container
    codeblock.insertBefore(copyButton, codeblock.firstChild);

    // Wrap the codeblock with the container
    codeblock.parentNode.insertBefore(wrapper, codeblock);
    wrapper.appendChild(codeblock);
  })
});
