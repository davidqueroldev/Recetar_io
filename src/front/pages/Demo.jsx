// Import necessary components from react-router-dom and other parts of the application.
import { Link } from "react-router-dom";
import useGlobalReducer from "../hooks/useGlobalReducer";  // Custom hook for accessing the global state.

export const Demo = () => {
  // Access the global state and dispatch function using the useGlobalReducer hook.
  const { store, dispatch } = useGlobalReducer()

  return (
    <div className="max-w-2xl mx-auto p-4">
      <ul className="space-y-4">
        {/* Map over the 'todos' array from the store and render each item as a list element */}
        {store && store.todos?.map((item) => {
          return (
            <li
              key={item.id}  // React key for list items.
              className="flex flex-col sm:flex-row sm:items-center sm:justify-between bg-white rounded-lg shadow p-4 border"
              style={{ background: item.background }}>
              {/* Link to the detail page of this todo. */}
              <Link to={"/single/" + item.id} className="text-blue-600 hover:underline font-semibold mb-2 sm:mb-0">
                Link to: {item.title}
              </Link>
              <div className="flex flex-col sm:flex-row sm:items-center gap-4">
                <p className="text-gray-600 text-sm">Open file ./store.js to see the global store that contains and updates the list of colors</p>
                <button
                  className="bg-green-500 hover:bg-green-600 text-white font-semibold py-2 px-4 rounded-lg shadow transition-colors duration-200"
                  onClick={() => dispatch({
                    type: "add_task",
                    payload: { id: item.id, color: '#ffa500' }
                  })}
                >
                  Change Color
                </button>
              </div>
            </li>
          );
        })}
      </ul>
      <br />
      <Link to="/">
        <button className="bg-blue-600 hover:bg-blue-700 text-white font-semibold py-2 px-6 rounded-lg shadow transition-colors duration-200">
          Back home
        </button>
      </Link>
    </div>
  );
};
