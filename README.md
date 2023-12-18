# Track Tales Community

#### /input responsive screenshot/

Explore Track Tales, a thoughtfully designed platform for seamless storytelling. Create posts with titles, rich content, and holiday tags. Personalize your profile, adding a unique touch, while geographical tags provide a global context. Interact seamlessly with likes and comments, fostering a sense of community. Join us in the beautifully crafted space of Track Tales and effortlessly share your stories.

The TrackTales community is live, to access it [click here.][ADD LINK]

## Table of contents

+ [UX](#ux)
+ [Design](#design)
+ [Features](#features)
+ [Testing](#testing)
+ [Technologies used](#technologies-used)
+ [Deployment](#deployment)
+ [Credits](#credits)

## UX

### Site Purpose
Track Tales serves as a dedicated space for individuals passionate about travel to freely share their stories. Our platform is designed to empower users, allowing them to create personalized profiles, seamlessly publish travel narratives, and engage with a community of like-minded travelers.

### Audience

Track Tales caters to travel enthusiasts and storytellers alike, providing a dedicated space for individuals passionate about sharing their unique travel experiences. This platform fosters connections among like-minded individuals who appreciate the beauty of diverse narratives from around the world, creating a vibrant community for bloggers and writers focused on the art of travel storytelling.

### Current User Goals
At Track Tales, users share their travel experiences, creating personalized profiles to showcase stories. Engaging with a global community, users explore diverse narratives, connect with like-minded enthusiasts, and manage their content effortlessly. Geographical tagging adds depth to stories, offering insights into different cultures and locations. The platform is designed to facilitate seamless storytelling and connections among individuals passionate about travel.

### Future User Goals
As Track Tales evolves, future users will likely seek a seamless space to share evolving travel experiences, connect with like-minded enthusiasts, and explore narratives that transcend geographical boundaries. The platform aims to continually enhance features, offering users intuitive tools for content management and community engagement in the realm of travel storytelling.

## Design

### Color scheme

### Typography

### Imagery

## Features

### Existing Features

### Future Features

## Testing

### Methodology 

Insert methodology here**

### User Stories 

#### Index page

| Testing  | Steps | Expected Outcome | Results |  
| - | - | - | - |
| Navigation bar functionality (user not authenticated) | Test that all links work | User is directed respectively to the home, about us, board, contact or account registration links | PASS |
| Navigation bar functionality (user authenticated) | Test that all links work | User is directed respectively to the navbar links and has the correct account links (profile and logout) | PASS |
| Footer links | Test that all links work and open a new tab when clicked | User is directed respectively to all social media links with  | PASS |
| Carrousel links | Test that all links work and redirect the user to the board, sing | User is directed respectively to all social media links with  | PASS |

#### About us page

| Testing  | Steps | Expected Outcome | Results |  
| - | - | - | - |
| "Start Exploring" button | Test that the links redirects to the post board | User is directed succesfully to the post board page | PASS |

#### Board
| Testing  | Steps | Expected Outcome | Results |  
| - | - | - | - |
| Filter post functionality | Test multiple filters from a single category and both categories. Clear filters button clear all selected filters.  | Post are successfully filter depending the applied filters. The clear filter button clears all selected filters. | PASS |
| Sign-in button display and functionality (user not authenticated) | The first card displayed above the displays a button to sign up, and the button redirects to sign-in form.  | Card successfully displays button and the button redirects to sign-in page | PASS |
| Like and comment buttons (user not authenticated) | When a not-authenticated user tries to like or comment on a post, a message is displayed stating that they need to login to performed any of those actions. The message contains an login link. | The buttons successfully toggle the login request message and the login link redirects to the login page. | PASS |
| Create post form (user authenticated) | The create post form is displayed with the username username at displayed at the top of the form. | When user is authenticated, the create post form is successfully displayed with the correct sign-in user at the top | PASS |
| Create post form - Form validation | Submit an empty form | The browser promts validation that all fields need to be filled. | PASS |
| Create post form - Form validation | Submit an form with an existing title. | An error message is displayed, stating that there is already a post with that title. | PASS |
| Create post form - Form validation | Submit an incomplete form. | The browser promts validation that all fields need to be filled. | PASS |
| Create post form - Form validation | Submit a complete post. | The post is successfully submited and a success message is displayed, stating that the post is awaiting review. | PASS |
| Post buttons - Like button | When the post is not liked by the authenticated user, the heart icon should be no solid, and when it is, it should be solid. When the post is liked or unliked, the counter should add up or substract down the number of likes and change the fill of the icon. | the button successfully adds or substracts the number of likes and the heart icon changes depending on the like status for that user. | PASS |
| Post buttons - Comment button | The comment button toggles a comment field area where the user can comment in the post. | The button successfuly toggles the comment area and the submit comment button. | PASS |
| Post buttons - Options dropdown button | When the authenticated user is the author of any of the posts, an option dropdown button should be displayed in the top right corner of the card. The dropdown should display two options: edit post and delete post. | The button is successfully displayed for posts where the authenticated user is the author but is not displayed for posts where the authenticated user is not the autor. | PASS |
| Comment form - Form validation | Submit an empty comment. | The browser promts validation that all fields need to be filled. | PASS |
| Comment form - Form validation | Submit a comment. | The comment is successfully submited an a success message is displayed, stating that the comment is awaiting review. | PASS |
| Post options - Edit post | When the post options is available, the edit post button displays a edit post modal with the correspondent post title at the top and the form to edit the post. | When the authenticated user is the author, it successfully displays the edit post modal when clicking the edit post option. | PASS |
| Post options - Delete post | When the post options is available, the delete post button displays a delete post modal with the correspondent post title at the top and the a button to delete the post. | When the authenticated user is the author, it successfully displays the delete post modal when clicking the delete post option. | PASS |
| Edit post - Form validation | Submit an empty form. | An error message is displayed, stating that fields are are required. | PASS |
| Edit post - Form validation | Submit an incomplete form. | An error message is displayed, stating that all fields are are required. | PASS |
| Edit post - Form validation | Submit an valid form. | A success message is displayed, stating that the post was successfully received and is awating for approval. | PASS |
| Delete post functionality | Click on delete post. | The post is successfully deleted and a success message is displayed confirming tha the post has been deleted. | PASS |

#### Contact 

| Testing  | Steps | Expected Outcome | Results |  
| - | - | - | - |
| Contact form - Form Validation | Submit empty form | Browser promts that required fields need to be filled | PASS |
| Contact form - Form Validation | Submit empty form (after filling and deleting the field's content) | Browser promts that required fields need to be filled | PASS |
| Contact form - Form Validation | Submit with an invalid email address | Error message is successfully displayed | PASS |
| Contact form - Form Validation | Submit valid form | User is redirect to success page stating that the response has been recorded | PASS |
| Contact form success links | Test the Sign up and home links functionality | User is successfully redirected to signup or home page | PASS |

#### Registration 

#### Profile
| Testing  | Steps | Expected Outcome | Results |  
| - | - | - | - |


## Technologies used

### Programming languages

- HTML5
- CSS
- JavaScript (jQuery)
- Python (Django)

### Frameworks, Libraries and programs used

- Google Fonts 
- Bootstrap
- Github
- CodeAnywhere
- Heroku
- cloudinary
- dj-database-url
- dj3-cloudinary-storage
- Django
- django-allauth
- guinicorn
- psychopg2


## Deployment

## Credits

### Design

### Code

### Media
