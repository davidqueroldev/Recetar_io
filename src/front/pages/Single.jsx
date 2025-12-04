// Import necessary hooks and components from react-router-dom and other libraries.
import { Link, useParams } from "react-router-dom";  // To use link for navigation and useParams to get URL parameters
import PropTypes from "prop-types";  // To define prop types for this component
import rigoImageUrl from "../assets/img/rigo-baby.jpg"  // Import an image asset
import useGlobalReducer from "../hooks/useGlobalReducer";  // Import a custom hook for accessing the global state

// Define and export the Single component which displays individual item details.
export const Single = props => {
  // Access the global state using the custom hook.
  const { store } = useGlobalReducer()

  // Retrieve the 'theId' URL parameter using useParams hook.
  const { theId } = useParams()
  const singleTodo = store.todos.find(todo => todo.id === parseInt(theId));

  return (
    <div className="max-w-xl mx-auto text-center p-6">
      {/* Display the title of the todo element dynamically retrieved from the store using theId. */}
      <h1 className="text-4xl font-bold mb-4">Todo: {singleTodo?.title}</h1>
      <hr className="my-6 border-gray-300" />  {/* A horizontal rule for visual separation. */}

      {/* A Link component acts as an anchor tag but is used for client-side routing to prevent page reloads. */}
      <Link to="/">
        <span className="inline-block bg-blue-600 hover:bg-blue-700 text-white font-semibold py-2 px-6 rounded-lg shadow transition-colors duration-200 cursor-pointer">
          Back home
        </span>
      </Link>
    </div>
  );
};

// Use PropTypes to validate the props passed to this component, ensuring reliable behavior.
Single.propTypes = {
  // Although 'match' prop is defined here, it is not used in the component.
  // Consider removing or using it as needed.
  match: PropTypes.object
};
