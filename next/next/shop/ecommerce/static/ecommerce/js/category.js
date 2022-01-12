        this.get_all_base_pagination = function () {

            _this = this;

            /* Check if our hidden form input is not empty, meaning it's not the first time viewing the page. */
            if ($('form.post-list input').val()) {
                /* Submit hidden form input value to load previous page number */
                data = JSON.parse($('form.post-list input').val());
                _this.ajax_get_all_base_pagination(data.page, data.name, data.sort);
            } else {
                /* If there's a page set in the URL, we load it. */
                page = 1;
                page_from_url = get_url_value('page');
                if (page_from_url) {
                    page = page_from_url;
                }

                /* Load first page */
                _this.ajax_get_all_base_pagination(page, $('.post_name').val(), $('.post_sort').val());
            }

            /* Search */
            $('body').on('click', '.post_search_submit', function () {
                _this.ajax_get_all_base_pagination(1, $('.post_name').val(), $('.post_sort').val());
            });
            /* Search when Enter Key is triggered */
            $(".base_search_text").keyup(function (e) {
                if (e.keyCode == 13) {
                    _this.ajax_get_all_base_pagination(1, $('.post_name').val(), $('.post_sort').val());
                }
            });

            /* Pagination Clicks   */
            $('body').on('click', '.pagination-nav li.active', function () {
                var page = $(this).attr('p');
                _this.ajax_get_all_base_pagination(page, $('.post_name').val(), $('.post_sort').val());
            });
        }

        /**
         * AJAX front-end base pagination.
         */
        this.ajax_get_all_base_pagination = function (page, order_by_name, order_by_sort) {

            if ($(".pagination-container").length > 0 && $('.products-view-all').length > 0) {
                $(".pagination-container").html(item_pagination_preloader());

                var post_data = {
                    page: page,
                    search: $('.post_search_text').val(),
                    name: order_by_name,
                    sort: order_by_sort,
                    max: $('.post_max').val(),
                };

                $('form.post-list input').val(JSON.stringify(post_data));

                var data = {
                    action: 'get-all-products',
                    csrfmiddlewaretoken: $("input[name=csrfmiddlewaretoken]").val(),
                    data: JSON.parse($('form.post-list input').val())
                };

                $.ajax({
                    url: module_path + 'products/',
                    type: 'POST',
                    data: data,
                    success: function (response) {
                        if ($(".pagination-container").html(response.content)) {
                            $('.pagination-nav').html(response.navigation);
                            scroll_to("body")
                            $('.table-post-list th').each(function () {
                                /* Append the button indicator */
                                $(this).find('i.fas').remove();
                                if ($(this).hasClass('active')) {
                                    if (JSON.parse($('form.post-list input').val()).th_sort == 'DESC') {
                                        $(this).append(' <i class="fas fa-chevron-down float-right"></i>');
                                    } else {
                                        $(this).append(' <i class="fas fa-chevron-up float-right"></i>');
                                    }
                                }
                            });
                        }
                    }
                });
            }
        }
