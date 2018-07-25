function signMeOut() {
    console.log('Signing out...');
    var auth2 = gapi.auth2.getAuthInstance();
    auth2.signOut().then(function () {
        console.log('User signed out.');
        window.setTimeout(function () {
            location.href = "index.html";
        }, 1);
    });

}
function Init() {
    console.log('Init...');
    gapi.load('auth2', function () {
        gapi.auth2.init();
    });
}
