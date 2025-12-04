import { Link } from "react-router-dom";

export const Navbar = () => {

	return (
		<nav className="bg-white border-b border-gray-200 shadow-sm">
			<div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 flex items-center justify-between h-16">
				<Link to="/">
					<span className="text-xl font-bold text-gray-800">React Boilerplate</span>
				</Link>
				<div>
					<Link to="/demo">
						<button className="bg-blue-600 hover:bg-blue-700 text-white font-semibold py-2 px-4 rounded-lg shadow transition-colors duration-200">
							Check the Context in action
						</button>
					</Link>
				</div>
			</div>
		</nav>
	);
};