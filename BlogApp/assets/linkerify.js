const firstname = document.querySelector('input[name=First_Name]');
const lastname = document.querySelector('input[name=Last_Name]');
const linker = document.querySelector('input[name=linker]');

const linkerify = (val) => {

    return val.toString().toLowerCase().trim()
        .replace(/&/g, '-and-')         // Replace & with 'and'
        .replace(/[\s\W-]+/g, '-')      // Replace spaces, non-word characters and dashes with a single dash (-)

};

titleInput.addEventListener('keyup', (e) => {
    slugInput.setAttribute('value', slugify(titleInput.value));
});