# Catch Chronicle API Testing

[Go to README.md](../../README.md)

## User Story Testing

User story testing has been executed from an Admin point of view: 

**Test** | **Action** | **Expected Result** | **Actual Result**
-------- | ------------------- | ------------------- | -----------------
User Registration | Create, update & delete user | A user can be created, edited or deleted | Works as expected
User login | Change permissions | User permissions can be updated | Works as expected
User profile | Create, update & delete | User profile can be created, edited or deleted | Works as expected
Catches | Create, update & delete | A catches can be created, edited or deleted | Works as expected
Comments | Create, update & delete | A comment can be created, edited or deleted | Works as expected
Follow/Unfollow | Create & delete |  Users can follow/unfollow other users | Works as expected
Notifications | User-specific notifications created from users follow, comment and likes | A notifications are being dynamically created| Works as expected
Likes | Create & delete | A catch can be liked/un-liked | Works as expected

Test for [Test for User story #1](https://github.com/alexelbert/catch-chronicle-api/issues/1)

<details>
  <summary>Show detailed results</summary>
    User Story: As a developer, I want to be able to create, read, update, and delete user profiles.

    **Test Steps:**
    - Logged in as admin i have CRUD for users
    **Expected Results:**
    - Able to have full CRUD functionality as admin for users
    
    **Screenshots**
        
    ![User Result](/docs/screenshots/usercrud.png)

    <hr>
    
    ![User Result](/docs/screenshots/usercrud2.png)

<hr>
  
  ![User Result](/docs/screenshots/usercrud3.png)

<hr>
  
  ![User Result](/docs/screenshots/usercrud4.png)

<hr>
  
  ![User Result](/docs/screenshots/usercrud5.png)

<hr>
  
  ![User Result](/docs/screenshots/usercrud6.png)
</details>

<hr>

Test for [Test for User story #8](https://github.com/alexelbert/catch-chronicle-api/issues/8)

<details>
  <summary>Show detailed results</summary>
  User Story: As a developer I want to be able to create, read, update and delete catches.

  **Test Steps:**
  - Logged in as admin i have CRUD for catches
  **Expected Results:**
  - Able to have full CRUD functionality as admin for catches
  
  **Screenshots**
    
  ![Catches Result](/docs/screenshots/catchescrud1.png)

  <hr>
  
  ![Catches Result](/docs/screenshots/catchescrud2.png)


<hr>
  
  ![Catches Result](/docs/screenshots/catchescrud3.png)


<hr>
  
  ![Catches Result](/docs/screenshots/catchescrud4.png)

</details>

<hr>

Test for [Test for User story #5](https://github.com/alexelbert/catch-chronicle-api/issues/5)

<details>
  <summary>Show detailed results</summary>
  User Story: As a developer, I want access to create, read, update, and delete comments.

  **Test Steps:**
  - Logged in as admin i have CRUD for comments
  **Expected Results:**
  - Able to have full CRUD functionality as admin for comments
  
  **Screenshots**
    
  ![Comments Result](/docs/screenshots/commentcrud.png)

  <hr>
  
  ![Comments Result](/docs/screenshots/commentcrud2.png)


<hr>
  
  ![Comments Result](/docs/screenshots/commentcrud3.png)

</details>

<hr>

Test for [Test for User story #6](https://github.com/alexelbert/catch-chronicle-api/issues/6)

<details>
  <summary>Show detailed results</summary>
  User Story: As a developer, I want access to create, read, update, and delete follow/unfollow relations between users.

  **Test Steps:**
  - Logged in as admin i have CRUD for follow/unfollow
  **Expected Results:**
  - Able to have full CRUD functionality as admin for follow/unfollow
  
  **Screenshots**
    
  ![Follow/Unfollow Result](/docs/screenshots/follow-unfollow-crud.png)

  <hr>
  
  ![Follow/Unfollow Result](/docs/screenshots/follow-unfollow-crud2.png)

</details>

<hr>

Test for [Test for User story #4](https://github.com/alexelbert/catch-chronicle-api/issues/4)

<details>
  <summary>Show detailed results</summary>
  User Story: As a developer, I want access to create, read, update and delete likes.

  **Test Steps:**
  - Logged in as admin i have CRUD for like
  **Expected Results:**
  - Able to have full CRUD functionality as admin for like
  
  **Screenshots**
    
  ![Like Result](/docs/screenshots/likescrud.png)

  <hr>
  
  ![Like Result](/docs/screenshots/likescrud2.png)

</details>

<hr>

Test for [Test for User story #7](https://github.com/alexelbert/catch-chronicle-api/issues/7)

<details>
  <summary>Show detailed results</summary>
  User Story: As a developer I want notifications to be created automatically when comments, likes, follows are created.

  **Test Steps:**
  - Logged in as admin can see dynamically created notifications and delete
  **Expected Results:**
  - Able to have full CRUD functionality as admin for notifications
  
  **Screenshots**
    
  ![Like Result](/docs/screenshots/notifications.png)

  <hr>
  
  ![Like Result](/docs/screenshots/notifications2.png)

</details>

<hr>


## Automated Testing

All Python code written for the project has been tested by writing automated unit tests using the testing features implemented in Django and Django Rest Framework ([Testing in Django](https://docs.djangoproject.com/en/4.2/topics/testing/), [Testing in DRF](https://www.django-rest-framework.org/api-guide/testing/)).

The output from running automated tests in the terminal:

```
❯ python3 manage.py test
Creating test database for alias 'default'...
System check identified no issues (0 silenced).

catch_chronicle.tests.CurrentUserSerializerTestCase.test_current_user_serializer
.
catches.tests.CatchDetailViewTests.test_authenticated_user_can_update_owned_catch
.
catches.tests.CatchDetailViewTests.test_get_invalid_catch
.
catches.tests.CatchDetailViewTests.test_get_valid_catch
.
catches.tests.CatchDetailViewTests.test_user_can_delete_owned_catch
.
catches.tests.CatchDetailViewTests.test_user_cannot_delete_unowned_catch
.
catches.tests.CatchDetailViewTests.test_user_cannot_update_another_users_catch
.
catches.tests.CatchListViewTests.test_user_can_list_catches
.
comments.tests.CommentDetailTest.test_user_can_delete_own_comment
.
comments.tests.CommentDetailTest.test_user_can_retrieve_comment
.
comments.tests.CommentDetailTest.test_user_can_update_own_comment
.
comments.tests.CommentDetailTest.test_user_cannot_delete_another_users_comment
.
comments.tests.CommentListTest.test_logged_in_user_can_create_comment
.
comments.tests.CommentListTest.test_logged_out_user_cannot_create_comment
.
comments.tests.CommentListTest.test_user_can_list_comments
.
followers.tests.FollowDetailTest.test_user_can_delete_own_follow
.
followers.tests.FollowDetailTest.test_user_can_retrieve_follow
.
followers.tests.FollowDetailTest.test_user_cannot_delete_another_users_follow
.
followers.tests.FollowListTest.test_logged_in_user_can_create_follow
.
followers.tests.FollowListTest.test_logged_out_user_cannot_create_follow
.
followers.tests.FollowListTest.test_user_can_list_follows
.
followers.tests.FollowListTest.test_user_cannot_follow_same_user_twice
.
likes.tests.LikeDetailTest.test_user_can_unlike_catch
.
likes.tests.LikeDetailTest.test_user_cannot_delete_another_users_like
.
likes.tests.LikeListTest.test_logged_in_user_can_like_catch
.
likes.tests.LikeListTest.test_logged_out_user_cannot_like_catch
.
likes.tests.LikeListTest.test_user_can_list_likes
.
notifications.tests.NotificationTests.test_list_notifications
.
notifications.tests.NotificationTests.test_mark_notification_as_read
.
notifications.tests.NotificationTests.test_notification_detail_view
.
notifications.tests.NotificationTests.test_unauthorized_access
.
profiles.tests.ProfileSerializerTest.test_get_follow_id_method_returns_follow_id
testuser1 testuser2
.
profiles.tests.ProfileSerializerTest.test_get_follow_id_method_returns_none_if_not_logged_in
.
----------------------------------------------------------------------
Ran 33 tests in 2.683s

OK
Destroying test database for alias 'default'...
```


## Manual Testing

- All API endpoints were manually tested with the browsable API interface with [Postman](https://www.postman.com/) for the deployed version (the documentation generated by Postman can be found here: [Postman API documentation](https://documenter.getpostman.com/view/33181094/2sA3Bg9aGx)).
- The API is working as expected.

## PEP 8 Linter

All python code written for the project passes through the PEP 8 [python linter](https://pep8ci.herokuapp.com/) by Code Institute without issues.

## Bugs

### Fixed Bugs

| Bug | Fix | Commit |
|---|---|---|
| There was an issue with dj-rest-auth-logout in version 5 of Django. Resulting in users not being able to log out. | Fixed by downgrading Django version, django-allauth and dj-rest-auth for better compatibility. | [Commit](https://github.com/alexelbert/catch-chronicle-api/commit/de66a8653a2d17a1c864f3b5c04540ef10dfbcf8) |
| There was an issue after downgrading python version and reinstalling matching versions for Django and Corsheaders. | Fix from [Stack Owerflow](https://stackoverflow.com/questions/77012106/django-allauth-modulenotfounderror-no-module-named-allauth-account-middlewar/77036615#77036615) where due to version control ```'allauth.account.middleware.AccountMiddleware',``` had to be removed.  | [Commit](https://github.com/alexelbert/catch-chronicle-api/commit/5a86f7f16213204a5b8d0e72381bfd5fa987abd9) |
| There was an issue with comments displaying on all catches across the whole site. | Fixed by renaming model field from from catch to catchId linked to comments including the filterset fields to be able to filter the comments to the correct catch. | [Commit 1](https://github.com/alexelbert/catch-chronicle-api/commit/f3e78b66e9452e8a0f2ccb403e2cb3acbb2f1274) [Commit 2](https://github.com/alexelbert/catch-chronicle-api/commit/ab81af48ddeb4de77ef961017cca867423b5dde0) [Commit 3](https://github.com/alexelbert/catch-chronicle-api/commit/c30f100583e722175247165051d2c2d2e9da7772) |




### Unfixed Bugs and Known Limitations

There is an issue with loading times for the frontend when rendering all catches from one user takes almost 8.5 seconds to fetch. This happens due to the pagination default setting. Due to the frontend making multiple request and making and calculating the information only in the frontend it would have been a better solution to fix this problem in the backend specifying multiple pagination classes. This is something to implement for the future. I managed to make slight improvement of rendering the data in 6.8 seconds increasing the pagination from 10 to 15 for the page size, this was a middle ground since it increases the rendering of catches by 0.5 seconds.
```    
'DEFAULT_PAGINATION_CLASS':
        'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 15,
    'DATETIME_FORMAT': '%d %b %Y',
 ```


