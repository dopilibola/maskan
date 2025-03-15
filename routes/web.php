<?php

use App\Http\Controllers\CemeteryController;
use App\Http\Controllers\DeceasedController;
use App\Http\Controllers\ProfileController;
use Illuminate\Support\Facades\Route;

Route::get('/', function () {
    return view('welcome');
});

// Dashboard (Requires Login)
Route::get('/dashboard', function () {
    return view('dashboard');
})->middleware(['auth', 'verified'])->name('dashboard');

// Protect routes (only logged-in users can access)
Route::middleware(['auth'])->group(function () {

    // Profile Routes
    Route::get('/profile', [ProfileController::class, 'edit'])->name('profile.edit');
    Route::patch('/profile', [ProfileController::class, 'update'])->name('profile.update');
    Route::delete('/profile', [ProfileController::class, 'destroy'])->name('profile.destroy');

    // Admin Panel Redirect
    Route::get('/admin', function () {
        return redirect()->route('cemeteries.index');
    });

    // Cemeteries (Only for logged-in users)
    Route::resource('cemeteries', CemeteryController::class);

    // Deceased (Only for logged-in users)
    Route::resource('deceased', DeceasedController::class);
});

require __DIR__.'/auth.php';
