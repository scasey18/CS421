var main = function (toDoObjects) {
    "use strict";
    var tabNumber;

    var toDos = toDoObjects.map(function (toDo) {
        // we'll just return the description
        // of this toDoObject
        return toDo.description;
    });

    var organizeByTags = function (toDoObjects) {
        // create an empty tags array
        var tags = [];
        // iterate over all toDos
        toDoObjects.forEach(function (toDo) {
            // iterate over each tag in this toDo
            toDo.tags.forEach(function (tag) {
                // make sure the tag is not already
                // in the tag array
                if (tags.indexOf(tag) === -1) {
                    tags.push(tag);
                }
            });
        });
        console.log(tags);
        var tagObjects = tags.map(function (tag) {
            // here we find all the to-do objects
            // that contain that tag
            var toDosWithTag = [];
            toDoObjects.forEach(function (toDo) {
                // check to make sure the result
                // of indexOf is *not* equal to -1
                if (toDo.tags.indexOf(tag) !== -1) {
                    toDosWithTag.push(toDo.description);
                }
            });
            // we map each tag to an object that
            // contains the name of the tag and an array
            return { "name": tag, "toDos": toDosWithTag };
        });
        console.log(tagObjects);
        return tagObjects;
    };

    $(".tabs a span").toArray().forEach(function (element) {
        // create a click handler for this element
        var $element = $(element);
        $(element).on("click", function () {
            $(".tabs a span").removeClass("active");
            $(element).addClass("active");
            $("main .content").empty();
            var $content;
            if ($element.parent().is(":nth-child(1)")) {
                $content = $("<ul>");
                toDos.forEach(function (todo) {
                    $content.append($("<li>").text(todo));
                });
                $("main .content").append($content);
            } else if ($element.parent().is(":nth-child(2)")) {
                $content = $("<ul>");
                toDos.reverse();
                toDos.forEach(function (todo) {
                    $content.append($("<li>").text(todo));
                });
                toDos.reverse();
                $("main .content").append($content);
            }
            else if ($element.parent().is(":nth-child(3)")) {
                var organizedByTag = organizeByTags(toDoObjects);
                organizedByTag.forEach(function (tag) {
                    var $tagName = $("<h3>").text(tag.name),
                        $content = $("<ul>");
                    tag.toDos.forEach(function (description) {
                        var $li = $("<li>").text(description);
                        $content.append($li);
                    });
                    $("main .content").append($tagName);
                    $("main .content").append($content);
                });
            }
            else if ($element.parent().is(":nth-child(4)")) {
                var $input = $("<input>").addClass("description"),
                    $inputLabel = $("<p>").text("Description: "),
                    $tagInput = $("<input>").addClass("tags"),
                    $tagLabel = $("<p>").text("Tags: "),
                    $button = $("<button>").text("+");

                $button.on("click", function () {
                    var description = $input.val(),
                        tags = $tagInput.val().split(","),
                        // create the new to-do item
                        newToDo = { "description": description, "tags": tags };
                    $.post("todos", newToDo, function (result) {
                        console.log(result);
                        // we'll wait to push the new object
                        // on the client until after the server
                        // returns
                        toDoObjects.push(newToDo);
                        // update toDos
                        toDos = toDoObjects.map(function (toDo) {
                            return toDo.description;
                        });
                        $input.val("");
                        $tagInput.val("");
                    });
                });

                $("main .content").append($inputLabel).append("<br>");
                $("main .content").append($input).append("<br>");
                $("main .content").append($tagLabel).append("<br>");
                $("main .content").append($tagInput);
                $("main .content").append($button);
            }
            return false;
        });
    });
    $(".tabs a:first-child span").trigger("click");
};
$(document).ready(function () {
    $.getJSON("todos.json", function (toDoObjects) {
        main(toDoObjects);
    });
});

//To get the json request working
//I followed instructions at this location
//https://www.thepolyglotdeveloper.com/2014/08/bypass-cors-errors-testing-apis-locally/