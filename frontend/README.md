# Frontend Service

## Overview

This frontend service is structured to support various functionalities including user interface, article parsing, and seamless integration with the backend API. It is designed with modularity and scalability.

## Directory Structure

- `node_modules/`: It shows up after running `npm install` and contains all the dependencies.
- `public/`: Contains static files for the application.
  - `fav.ico`: Application icon.
- `src/`: Main application directory.
  - `assets/`: Contains static assets such as images, icons, and styles.
    - `base.css`: Base styles for the application.
    - `main.css`: Main styles for the application, automatically import `base.css`.
  - `components/`: Contains reusable Vue components.
    - `DashboardCard.vue`: Card component used in the dashboard page for displaying available actions.
    - `PaperList.vue`: List component for displaying a list of papers related to a search query.
    - `SearchResult.vue`: Pop-up window component for displaying search results.
    - `UserChip.vue`: Chip component for displaying user information.
  - `layouts/`: Contains layout components for different pages.
    - `BaseLayout.vue`: Base layout component for the application, including sidebar, app bar, and main content area.
    - `NetLayout.vue`: Layout component for the network page with two available slots.
  - `lib/`: Contains utility functions and classes.
    - `routesConfig.js`: Configuration file for the application routes.
    - `exampleXXX.json`: Example JSON files for testing purposes.
    - `searchResults.js`: Example search results for testing purposes.
  - `router/`: Contains the Vue router configuration.
    - `index.js`: Vue router configuration file.
  - `utils/`: Contains utility functions and classes.
    - `network.js`: Network utility functions.
  - `views/`: Contains page components.
    - `author/`: Contains author-related page components.
      - `AuthorAffiliation.vue`: Author affiliation page.
      - `CoAuthors.vue`: Co-authors page.
    - `reference/`: Contains reference-related page components.
      - `CitedByTree`: Cited by tree page.
      - `CitedTree.vue`: Cited tree page.
    - `topic/`: Contains topic-related page components.
      - `SameTopic.vue`: Same topic page.
      - `TopicConnection.vue`: Topic connection page.
    - `ErrorPage.vue`: Error page.
    - `PaperDashboard.vue`: Dashboard page.
  - `App.vue`: Main application component.
  - `main.js`: Entry point of the application.
- `tests/`: Contains unit tests.
  - `components/`: Contains unit tests for components.
    - `DashboardCard.test.js`: Test cases for the `DashboardCard` component.
    - `PaperList.test.js`: Test cases for the `PaperList` component.
    - `SearchResult.test.js`: Test cases for the `SearchResult` component.
    - `UserChip.test.js`: Test cases for the `UserChip` component.
  - `views/`: Contains unit tests for views.
    - `ErrorPage.test.js`: Test cases for the `ErrorPage` view.
    - `PaperDashboard.test.js`: Test cases for the `PaperDashboard` view.
  - `setup.js`: Test setup file.
- `.env.development`: Environment variables for development.
- `.env.production`: Environment variables for production.
- `.eslintrc.cjs`: ESLint configuration file.
- `default.conf`: Configuration file for the Nginx server.
- `Dockerfile`: Docker configuration file.
- `index.html`: Main HTML file for the application.
- `jsconfig.json`: JavaScript configuration file.
- `package.json`: Project dependencies and scripts.
- `package-lock.json`: Lock file for project dependencies.
- `postcss.config.js`: PostCSS configuration file.
- `README.md`: This file.
- `tailwind.config.js`: Tailwind CSS configuration file.
- `vite.config.js`: Vite configuration file.

## Installation

> Please make sure the Node.js (>v20) and npm are available on your machine. Go [Setup.md](../Documents/Implementation/Setup.md#frontend-service) for more information

1. enter the `frontend` directory if still in root directory
   ```
   cd frontend
   ```
2. install dependencies
   ```
   npm install
   ```

## Running the Application in Development Mode

start the application in development mode
```
npm run dev
```
Now the application is running in development mode. Open [http://localhost:5173](http://localhost:5173) to view it in the browser.

## Testing

run tests using Vitest

```
npm test
```

## Deployment Preview (Optional)

1. build the application first

   ```
   npm run build
   ```

2. start the application deployment preview

   ```
   npm run preview
   ```

Now the application deployment preview is running. Open [http://localhost:4173](http://localhost:4173) to view it in the browser.




