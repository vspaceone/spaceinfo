

window.setInterval(function () {
    console.log("loading new page");
    $.getJSON("file:///home/max/git/spaceinfo/pages/directory.json", function (data) {
        var d = Math.floor((Math.random() * data.length));
        console.log(data[d].link);
        var newUrl = data[d].link;
        window.location.replace(newUrl);

    });
}, 2000);