<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class Cemetery extends Model
{
    use HasFactory;
    protected $fillable = ['name', 'location', 'deceased_count', 'available_spots', 'supervisor_name', 'supervisor_phone', 'property_info'];

    public function deceased()
    {
        return $this->hasMany(Deceased::class);
    }
}
