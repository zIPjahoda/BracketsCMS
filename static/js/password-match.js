$(() => {
    const passwordField = $("#id_password");
    const passwordAgainField = $("#id_password_again");

    const checkPasswords = () => {
        if(passwordField.val() !== passwordAgainField.val())
            changeFieldsColor("#FF0000");
        else changeFieldsColor("#00FF00");
    };

    const changeFieldsColor = (color) => {
        passwordField.css("background", color);
        passwordAgainField.css("background", color);
    };

    passwordField.change(checkPasswords);
    passwordAgainField.change(checkPasswords);
});