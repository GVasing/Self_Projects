// Base URL for API
const API_BASE_URL = "http://localhost:5500/api"

// Function to handle API requests
async function apiRequest(endpoint, options = {}) {
    try {
        const response = await fetch(`${API_BASE_URL}${endpoint}`, {
            headers:{
                "Content-Type": "application/json",
                ...options.headers,
            },
            ...options,
        });

        if (!response.ok){
            throw new Error(`HTTP Error.  Status: ${response.status}`);
        }

        return await response.json();
    } catch (error) {
        console.error("API request failed: ", error);
        throw error;
    }
}

// CRUD Operations
const toDoAPI = {
    // GET All ToDos
    getAll: async () => {
        return await apiRequest("/to_dos");
    },

    // GET ToDo Item by ID
    getById: async (id) => {
        return await apiRequest(`/to_dos/${id}`)
    },

    // POST ToDo Item
    create: async (toDoData) => {
        return await apiRequest("/to_dos", {
            method: "POST",
            body: JSON.stringify(toDoData),
        });
    },

    // PUT/PATCH ToDo Item
    update: async (id, toDoData) => {
        return await apiRequest(`/to_dos/${id}`, {
            method: "PATCH",
            body: JSON.stringify(toDoData),
        });
    },

    // DELETE ToDoItem
    delete: async (id) => {
        return await apiRequest(`/to_dos/${id}`, {
            method: "DELETE",
        });
    }
}