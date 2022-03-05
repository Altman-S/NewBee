export {
    validate_year
}

function validate_year (value) {
    // year from 1900 to 2023
    const re = new RegExp(/^(19[5-9]\d|20[0-4]\d|2050)$/);
    return re.test(value.trim());
}