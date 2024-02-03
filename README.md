# Web3 Product Registry App Documentation

## Overview

The Web3 Product Registry App is a Flask-based web application that interacts with a smart contract on the Ethereum blockchain. It allows users to register products, view all registered products, and change the holder of a product.

## Prerequisites

- Python 3.6 or higher
- Flask
- Web3.py
- Python-dotenv
- Solidity smart contract (ProductRegistry.json)

## Setup

1. **Install Dependencies:**
   ```bash
   pip install Flask web3 python-dotenv
   ```

2. **Smart Contract:**
   - Deploy the Solidity smart contract (ProductRegistry.json) to the Ethereum blockchain.
   - Obtain the contract address and ABI.

3. **Environment Variables:**
   - Create a `.env` file in the project directory with the following variables:
     ```dotenv
     RPC_URL=<Your Ethereum Node RPC URL>
     PRIVATE_KEY=<Your Ethereum Account Private Key>
     CONTRACT_ADDRESS=<Your Smart Contract Address>
     ```

## Running the App

1. **Run the Flask App:**
   ```bash
   python app.py
   ```
   The app will be accessible at http://localhost:8444/.

2. **Access the Web App:**
   Open your web browser and navigate to http://localhost:8444/.

## App Routes

- **/ (Home):**
  - Displays the total number of registered products.
  - Provides a form to register a new product.
  - Allows viewing all registered products.
  - Supports changing the holder of a product.

- **/registerProduct (POST):**
  - Handles the registration of a new product.
  - Expects form data: ID, Holder Name, Location, City, Vehicle.

- **/showAllProducts:**
  - Returns a JSON object containing details of all registered products.

- **/changeHolder (POST):**
  - Handles changing the holder of a product.
  - Expects form data: Product ID, New Holder Name.

## Smart Contract Functions

- **showAll:**
  - Returns the total number of registered products.

- **register:**
  - Registers a new product with the specified details.

- **changeHolder:**
  - Changes the holder of a product.

## Important Notes

- Ensure that the Ethereum node specified in `RPC_URL` is accessible and synchronized.
- The private key in `PRIVATE_KEY` must have sufficient Ether for gas fees.
- This documentation assumes a basic understanding of Ethereum, smart contracts, and Flask.

## Feel free to  raise your questions-
Mail-thouhedul.alam.tonoy@gmail.com

