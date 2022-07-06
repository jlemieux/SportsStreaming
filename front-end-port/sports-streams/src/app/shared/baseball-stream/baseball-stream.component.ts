import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { DomSanitizer, SafeResourceUrl } from '@angular/platform-browser';

@Component({
  selector: 'app-baseball-stream',
  templateUrl: './baseball-stream.component.html',
  styleUrls: ['./baseball-stream.component.css']
})
export class BaseballStreamComponent implements OnInit {

  link: SafeResourceUrl = '';

  constructor(private route: ActivatedRoute, private sanitizer: DomSanitizer) { }

  ngOnInit() {
    this.route.queryParams.subscribe(params => {
      // const uriDecoded = decodeURI(params.link);
      // const unsafe = atob(uriDecoded);
      const unsafe = decodeURI(params.link);
      this.link = this.sanitizer.bypassSecurityTrustResourceUrl(unsafe);
    });
  }

}
