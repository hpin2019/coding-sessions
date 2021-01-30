package com.example.quotesapp;

import androidx.appcompat.app.ActionBarDrawerToggle;
import androidx.appcompat.app.AppCompatActivity;
import androidx.appcompat.widget.Toolbar;
import androidx.drawerlayout.widget.DrawerLayout;
import androidx.fragment.app.Fragment;
import androidx.fragment.app.FragmentManager;

import android.content.Context;
import android.content.Intent;
import android.net.Uri;
import android.os.Bundle;
import android.view.MenuItem;
import android.view.View;
import android.widget.Toast;

import com.google.android.material.navigation.NavigationView;

public class MainActivity extends AppCompatActivity {

    // Drawer and Actionbar
    private DrawerLayout mDrawer;
    private Toolbar toolbar;
    private NavigationView nvDrawer;

    // Make sure to be using androidx.appcompat.app.ActionBarDrawerToggle version.
    private ActionBarDrawerToggle drawerToggle;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        setupActionBar();
    }


    private void setupActionBar() {
        // Set a Toolbar to replace the ActionBar.
        toolbar = (Toolbar)findViewById(R.id.toolbar);
        setSupportActionBar(toolbar);

        getSupportActionBar().setDisplayHomeAsUpEnabled(true);

        // Find our drawer view
        mDrawer = (DrawerLayout)findViewById(R.id.drawer_nav);
        // Setup toggle to display hamburger icon with animation
        drawerToggle = new ActionBarDrawerToggle(this, mDrawer, toolbar, R.string.navigation_drawer_open,  R.string.navigation_drawer_close);

        drawerToggle.setDrawerIndicatorEnabled(true);
        drawerToggle.syncState();

        // Attach DrawerLayout events to the ActionBarToggle
        mDrawer.addDrawerListener(drawerToggle);
        // Find our navigation view
        nvDrawer = (NavigationView)findViewById(R.id.nav_view);
        // Setup navigation view
        nvDrawer.setNavigationItemSelectedListener(
                new NavigationView.OnNavigationItemSelectedListener() {
                    @Override
                    public boolean onNavigationItemSelected(MenuItem menuItem) {
                        selectDrawerItem(menuItem);
                        return true;
                    }
                });
    }

    public void selectDrawerItem(MenuItem menuItem) {
        // Create a new fragment and specify the fragment to show based on nav item clicked
        Fragment fragment = null;
        Class fragmentClass = null;
        switch(menuItem.getItemId()) {
            case R.id.nav_rating:
                openPlaystore(this);
                break;
            case R.id.nav_share:
                shareApp();
                break;
            case R.id.nav_fb:
                openFB();
                break;
            case R.id.nav_pinterest:
                openPinterest();
                break;
            default:
                this.onBackPressed();
        }

        /*try {
            if(fragmentClass!=null) {
                fragment = (Fragment) fragmentClass.newInstance();
                // Insert the fragment by replacing any existing fragment
                FragmentManager fragmentManager = getActivity().getSupportFragmentManager();
                fragmentManager.beginTransaction().replace(R.id.fragment_container, fragment).commit();
                // Set action bar title
                ((AppCompatActivity)getActivity()).setTitle(menuItem.getTitle());
            }
        } catch (Exception e) {
            e.printStackTrace();
        }*/
        // Highlight the selected item has been done by NavigationView
        menuItem.setChecked(true);
        // Close the navigation drawer
        mDrawer.closeDrawers();
    }

    /*private  void openYTChannel(){

        String channelId = "UCkbDvKU1h1G3_ZQ1TJ0eF5g";
        Intent intent = YouTubeIntents.createChannelIntent(this,channelId);
        startActivity(intent);
    }

     */

    private void openPlaystore(Context context) {
        String playstoreUrl = "market://details?id=" + context.getPackageName();
        final Uri marketUri = Uri.parse(playstoreUrl);
        try {
            context.startActivity(new Intent(Intent.ACTION_VIEW, marketUri));
        } catch (android.content.ActivityNotFoundException ex) {
            Toast.makeText(context, "Couldn't find PlayStore on this device", Toast.LENGTH_SHORT).show();
        }
    }

    private void shareApp(){
        try {
            String playstoreUrl = "https://play.google.com/store/apps/details?id="+this.getPackageName();
            final Uri marketUri = Uri.parse(playstoreUrl);
            Intent shareIntent = new Intent(Intent.ACTION_SEND);
            shareIntent.setType("text/plain");
            shareIntent.putExtra(Intent.EXTRA_SUBJECT, "Beautiful Quotes App");
            String shareMessage= "Check out the Beautiful Quotes app\n\n";
            shareMessage = shareMessage + marketUri;
            shareIntent.putExtra(Intent.EXTRA_TEXT, shareMessage);
            startActivity(Intent.createChooser(shareIntent, "Share via"));
        } catch(Exception e) {
            //e.toString();
        }
    }

    private void openFB(){
        String url = "https://www.facebook.com/hellomorning2020/";
        goToUrl(url);
    }

    private void openPinterest(){
        String url = "https://in.pinterest.com/hpin2019/";
        goToUrl(url);
    }

    private void goToUrl(String url) {
        Uri uriUrl = Uri.parse(url);
        Intent launchBrowser = new Intent(Intent.ACTION_VIEW, uriUrl);
        startActivity(launchBrowser);
    }

}
