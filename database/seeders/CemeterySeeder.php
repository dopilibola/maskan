<?php

namespace Database\Seeders;

use App\Models\Cemetery;
use Illuminate\Database\Console\Seeds\WithoutModelEvents;
use Illuminate\Database\Seeder;

class CemeterySeeder extends Seeder {
    public function run() {
        Cemetery::create([
            'name' => 'Minor Cemetery',
            'address' => 'Mukumi Street, Tashkent',
            'deceased_count' => 511,
            'available_spots' => 457,
            'image' => 'https://via.placeholder.com/300'
        ]);
    }
}
