$(document).ready(() => {
    $('div#add_item').on('click', () => {
        $('<li>Item</li>').appendTo('ul.my_list')
    })

    $('div#remove_item').on('click', () => {
        // $('ul.my_list :last-child').remove();
        $('li').last().remove()
    })

    $('div#clear_list').on('click', () => {
        $('li').remove();
    })

})