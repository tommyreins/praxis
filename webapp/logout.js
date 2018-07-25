function signMeOut() {
    console.log('Signing out...');
    var auth2 = gapi.auth2.getAuthInstance();
    auth2.signOut().then(function () {
        console.log('User signed out.');
    });
}
function Init() {
    console.log('Init...');
    gapi.load('auth2', function () {
        gapi.auth2.init();
    });
}
