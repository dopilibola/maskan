<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class Deceased extends Model
{
    use HasFactory;
    protected $fillable = ['name', 'surname', 'region', 'district', 'city', 'cemetery_id', 'date_received', 'address'];

    public function cemetery()
    {
        return $this->belongsTo(Cemetery::class);
    }
}
