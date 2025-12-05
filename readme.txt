APIs as per the requirements:
/restaurant/booking/tables/
/restaurant/menu/ same as /restaurant/menu-items/ due to conflicting requirements
/message/
/api-token-auth/
/api-auth/
/auth/

Steps taken to create the app:

1. Static HTML content: index.html, images, css
2. Created MySQL database  LittleLemon, performed migrations, registered in Admin
3. Admin site: user admin, password 12345
4. Added api-auth
5. Added menu and booking models, added serializers, added views
    IMPORTANT: contradicting instructions provided - Menu and MenuItem, api vs restaurant endpoint
6. Added authtoken, migrated
7. Added protected message
8. djoser
9. Test