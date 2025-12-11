const API_URL = import.meta.env.VITE_BACKEND_URL;

// Function to register a new user
export const registerUser = async (email, password, role) => {
  try {
    const response = await fetch(`${API_URL}/api/auth/register`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ email, password, role }),
    });

    const data = await response.json(); // Parse JSON response

    if (!response.ok) {
      throw new Error(data.message || "Registration failed");
    }

    return data; // Return the response data
  } catch (error) {
    throw new Error(error.message || "Network error");
  }
};

// Function to log in a user
export const loginUser = async (email, password) => {
  try {
    const response = await fetch(`${API_URL}/api/auth/login`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ email, password }),
    });

    const data = await response.json();

    if (!response.ok) {
      throw new Error(data.message || "Login failed");
    }

    return data;
  } catch (error) {
    throw new Error(error.message || "Network error");
  }
};

// Function to get user profile
export const getUserProfile = async (token) => {
  try {
    const response = await fetch(`${API_URL}/api/auth/profile`, {
      method: "GET",
      headers: {
        Authorization: `Bearer ${token}`,
      },
    });

    const data = await response.json();

    if (!response.ok) {
      throw new Error(data.message || "Failed to fetch user profile");
    }

    return data;
  } catch (error) {
    throw new Error(error.message || "Network error");
  }
};
