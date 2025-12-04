import React, { Component } from "react";
import envFile from "../../../docs/assets/env-file.png"

const Dark = ({ children }) => <span className="bg-gray-800 text-white px-1.5 rounded-md text-sm font-mono">{children}</span>;
export const BackendURL = () => (
  <div className="mt-12 pt-12 w-full max-w-xl mx-auto">
    <h2 className="text-2xl font-bold mb-4">Missing BACKEND_URL env variable</h2>
    <p className="mb-2">Here's a video tutorial on <a target="_blank" rel="noopener noreferrer" href="https://www.awesomescreenshot.com/video/16498567?key=72dbf905fe4fa6d3224783d02a8b1b9c" className="text-blue-600 underline hover:text-blue-800">how to update your backend URL environment variable.</a></p>
    <p className="mb-2">There's a file called <Dark>.env</Dark> that contains the environmental variables for your project.</p>
    <p className="mb-2">There's one variable called <Dark>BACKEND_URL</Dark> that needs to be manually set by yourself.</p>
    <ol className="list-decimal list-inside mb-4 space-y-1 text-gray-700">
      <li>Make sure your backend is running on port 3001.</li>
      <li>Open your API and copy the API host.</li>
      <li>Open the .env file (do not open the .env.example)</li>
      <li>Add a new variable VITE_BACKEND_URL=<Dark>your api host</Dark></li>
      <li>Replace <Dark>your api host</Dark> with the public API URL of your flask backend server running at port 3001</li>
    </ol>
    <div className="w-full mb-4">
      <img src={envFile} className="w-full rounded shadow" alt=".env file example" />
    </div>
    <p className="text-sm text-gray-600">Note: If you are publishing your website to Heroku, Render.com or any other hosting you probably need to follow other steps.</p>
  </div>
);