<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>@yield('title', 'Maskan')</title>
    @vite('resources/css/app.css')
</head>
<body class="bg-gray-100">

<!-- Navbar -->
<nav class="bg-white shadow-md p-4 flex justify-between items-center">
    <div class="text-2xl font-bold text-gray-800">
        <a href="{{ route('cemeteries.index') }}" class="hover:text-blue-500 transition">MASKAN</a>
    </div>
    <div class="space-x-6">
        <a href="{{ route('cemeteries.index') }}" class="text-gray-700 hover:text-blue-500 transition">🪦 Cemeteries</a>
        <a href="{{ route('deceased.index') }}" class="text-gray-700 hover:text-blue-500 transition">⚰️ Deceased</a>
        <a href="{{ route('cemeteries.create') }}" class="text-green-600 hover:text-green-800 font-semibold transition">➕ Add Cemetery</a>
        <a href="{{ route('deceased.create') }}" class="text-green-600 hover:text-green-800 font-semibold transition">➕ Add Deceased</a>
    </div>
    <a href="{{ route('logout') }}" class="bg-red-600 text-white px-4 py-2 rounded-md shadow hover:bg-red-700 transition">
        🚪 Logout
    </a>
</nav>

<!-- Content -->
<div class="container mx-auto py-6 px-4">
    @yield('content')
</div>

</body>
</html>
