// Base URL for API
const API_BASE_URL = "http://localhost:5500"

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

// ToDo
const toDoAPI = {
    // GET All ToDos
    getAll: async () => {
        return await apiRequest("/to_dos/");
    },

    // GET ToDo Item by ID
    getById: async (id) => {
        return await apiRequest(`/to_dos/${id}`)
    },

    // POST ToDo Item
    create: async (toDoData) => {
        return await apiRequest("/to_dos/", {
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

// InProgress
const inProgressAPI = {
    // GET All In Progress Items
    getAll: async () => {
        return await apiRequest("/in_progresses/");
    },

    // GET In Progress Item by ID
    getById: async (id) => {
        return await apiRequest(`/in_progresses/${id}`);
    },

    // POST In Progress Item
    create: async (inProgressData) => {
        return await apiRequest("/in_progresses/", {
            method: "POST",
            body: JSON.stringify(inProgressData),
        });
    },

    // UPDATE (PATCH) In Progress Item
    update: async (id, inProgressData) => {
        return await apiRequest(`/in_progresses/${id}`, {
            method: "PATCH",
            body: JSON.stringify(inProgressData),
        });
    },

    // DELETE In Progress Item
    delete: async (id) => {
        return await apiRequest(`/in_progresses/${id}`, {
            method: "DELETE",
        });
    }
}

// Completed
const completedAPI = {
    // GET All Completed Items
    getAll: async () => {
        return await apiRequest("/completeds/");
    },

    // GET Completed Item by ID
    getById: async (id) => {
        return await apiRequest(`/completeds/${id}`);
    },

    // POST Completed Item
    create: async (completedData) => {
        return await apiRequest("/completeds/", {
            method: "POST",
            body: JSON.stringify(completedData),
        });
    },

    // UPDATE (PATCH) Completed Item
    update: async (id, completedData) => {
        return await apiRequest(`/completeds/${id}`, {
            method: "PATCH",
            body: JSON.stringify(completedData),
        });
    },

    // DELETE Completed Item
    delete: async (id) => {
        return await apiRequest(`/completeds/${id}`, {
            method: "DELETE",
        });
    }
}