package com.bangkit.capstoneproject.kudaur.ui.profile

import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.provider.Settings
import android.view.MenuItem
import com.bangkit.capstoneproject.kudaur.MainActivity
import com.bangkit.capstoneproject.kudaur.R
import com.bangkit.capstoneproject.kudaur.data.preferences.SessionPreference
import com.bangkit.capstoneproject.kudaur.databinding.ActivityProfileBinding

class ProfileActivity : AppCompatActivity() {

    private lateinit var session: SessionPreference
    private lateinit var binding: ActivityProfileBinding

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityProfileBinding.inflate(layoutInflater)
        setContentView(binding.root)
        supportActionBar?.setDisplayHomeAsUpEnabled(true)
        supportActionBar?.title = getString(R.string.profile)

        session = SessionPreference(applicationContext)

        binding.namaUser.text = session.getSession()?.name

        binding.editBahasa.setOnClickListener {
            startActivity(Intent(Settings.ACTION_LOCALE_SETTINGS))
        }

        binding.buttonLogout.setOnClickListener {
            SessionPreference(this).clearSession()
            val moveActivity = Intent(this@ProfileActivity, MainActivity::class.java)
            startActivity(moveActivity)
            finish()
        }
    }

    override fun onOptionsItemSelected(item: MenuItem): Boolean {
        return when (item.itemId) {
            android.R.id.home -> {
                finish()
                true
            }
            else -> true
        }
    }
}