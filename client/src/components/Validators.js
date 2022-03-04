export {
    validate_year
}

function validate_year (value) {
    // year from 1900 to 2099
    const re = new RegExp('^(19|20)\d{2}$');
    return re.test(value);
}